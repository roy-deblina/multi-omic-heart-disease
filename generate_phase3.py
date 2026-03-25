#!/usr/bin/env python3
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.ensemble import RandomForestClassifier

np.random.seed(42)

# Load Phase 1-2
phase2_features = pd.read_csv('mvp_results/integrated_features.csv', index_col=0)
phase2_subtypes = pd.read_csv('mvp_results/patient_subtypes.csv', index_col=0)

# Generate metabolites (250)
n_samples = phase2_features.shape[0]
n_metabolites = 250

metabolites = np.random.randn(n_samples, n_metabolites)
subtypes = phase2_subtypes.values.flatten()

for subtype in [0, 1, 2]:
    mask = subtypes == subtype
    metabolites[mask, :50] += np.random.normal(0.5 + subtype*0.3, 0.3, (mask.sum(), 50))
    metabolites[mask, 50:100] += np.random.normal(-0.5 + subtype*0.2, 0.3, (mask.sum(), 50))
    metabolites[mask, 100:150] += np.random.normal(0.8 - subtype*0.2, 0.3, (mask.sum(), 50))

metabolites_df = pd.DataFrame(metabolites, index=phase2_features.index, 
                             columns=[f'Metabolite_{i}' for i in range(1, n_metabolites+1)])

# Preprocess metabolites
metabolites_log = np.log2(np.abs(metabolites_df) + 1) * np.sign(metabolites_df)
scaler = StandardScaler()
metabolites_normalized = pd.DataFrame(scaler.fit_transform(metabolites_log), 
                                     index=metabolites_log.index, 
                                     columns=metabolites_log.columns)

# PCA: 250 -> 10
pca = PCA(n_components=10)
metabolites_pca = pca.fit_transform(metabolites_normalized)
metabolites_pca_df = pd.DataFrame(metabolites_pca, 
                                 index=metabolites_normalized.index, 
                                 columns=[f'Metabolite_PC{i+1}' for i in range(10)])

# Combine all layers
phase3_features = pd.concat([phase2_features, metabolites_pca_df], axis=1)

# K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=20)
phase3_clusters = kmeans.fit_predict(phase3_features)
sil_score = silhouette_score(phase3_features, phase3_clusters)

# Save results
phase3_features.to_csv('mvp_results/phase3_integrated_features.csv')
metabolites_pca_df.to_csv('mvp_results/metabolite_pca_components.csv')
pd.DataFrame(phase3_clusters, index=phase3_features.index, columns=['Subtype']).to_csv('mvp_results/phase3_patient_subtypes.csv')

# Feature importance
rf = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10)
rf.fit(phase3_features, phase3_clusters)
pd.DataFrame({'Feature': phase3_features.columns, 'Importance': rf.feature_importances_}).to_csv('mvp_results/phase3_feature_importance.csv', index=False)

# Biomarkers
biomarkers = pd.DataFrame({
    'Subtype': [0, 1, 2], 
    'Count': [np.sum(phase3_clusters==i) for i in range(3)]
})
biomarkers.to_csv('mvp_results/phase3_biomarkers.csv', index=False)

print('✅ Phase 3 Complete!')
print(f'   Features: {phase3_features.shape}')
print(f'   Silhouette: {sil_score:.4f}')
