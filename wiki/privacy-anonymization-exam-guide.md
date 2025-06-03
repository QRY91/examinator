# Privacy Anonymization Exam Guide

## 📚 Study Questions & Answers

### 1. What is the difference between privacy and confidentiality?

<details>
<summary>🤔 Click to reveal answer</summary>

Privacy is an individual's right to control how their personal data is used, while confidentiality is the obligation to keep information secret from unauthorized parties.

</details>

### 2. What is personally identifiable information (PII)?

<details>
<summary>🤔 Click to reveal answer</summary>

Any information that can be used to identify a specific individual, either directly (name, SSN) or indirectly (combination of attributes).

</details>

### 3. What are quasi-identifiers?

<details>
<summary>🤔 Click to reveal answer</summary>

Attributes that alone don't uniquely identify someone, but when combined with other data sources can lead to re-identification (e.g., age, ZIP code, gender).
### Data Anonymization Techniques

</details>

### 4. What is data anonymization?

<details>
<summary>🤔 Click to reveal answer</summary>

The process of removing or altering personally identifiable information so that individuals cannot be identified from the dataset.

</details>

### 5. What are the main anonymization techniques?

<details>
<summary>🤔 Click to reveal answer</summary>

1) Blanking (removing data), 2) Hashing (one-way transformation), 3) Masking (partial obscuring), 4) Generalization (making data less specific), 5) Suppression (removing records).

</details>

### 6. What is pseudonymization?

<details>
<summary>🤔 Click to reveal answer</summary>

Replacing identifying information with artificial identifiers (pseudonyms) while maintaining a separate mapping that can be reversed if needed.
### K-Anonymity

</details>

### 7. What is k-anonymity?

<details>
<summary>🤔 Click to reveal answer</summary>

A privacy preservation technique ensuring that each record in a dataset is indistinguishable from at least k-1 other records based on quasi-identifiers.

</details>

### 8. How do you achieve k-anonymity?

<details>
<summary>🤔 Click to reveal answer</summary>

1) Generalization (making values less specific, e.g., exact age → age ranges), 2) Suppression (removing outlier records), 3) Combination of both techniques.

</details>

### 9. What does k=3 anonymity mean?

<details>
<summary>🤔 Click to reveal answer</summary>

Every combination of quasi-identifier values appears at least 3 times in the dataset, so any individual is indistinguishable from at least 2 others.

</details>

### 10. What are the limitations of k-anonymity?

<details>
<summary>🤔 Click to reveal answer</summary>

1) Homogeneity attack (if all k records have same sensitive value), 2) Background knowledge attack, 3) Data utility loss through generalization.
### Advanced Privacy Techniques

</details>

### 11. What is l-diversity?

<details>
<summary>🤔 Click to reveal answer</summary>

An extension of k-anonymity that ensures each equivalence class has at least l different values for sensitive attributes, preventing homogeneity attacks.

</details>

### 12. What is t-closeness?

<details>
<summary>🤔 Click to reveal answer</summary>

Further refinement requiring that the distribution of sensitive attributes in each equivalence class is close to the overall distribution in the dataset.

</details>

### 13. What is differential privacy?

<details>
<summary>🤔 Click to reveal answer</summary>

A privacy technique that adds carefully calibrated random noise to query results, providing mathematical guarantees about privacy while preserving statistical utility.

</details>

### 14. What are the advantages of differential privacy over k-anonymity?

<details>
<summary>🤔 Click to reveal answer</summary>

1) Mathematical privacy guarantees, 2) Composability (multiple queries), 3) Resistance to auxiliary information attacks, 4) Better utility preservation.
### Privacy Attacks

</details>

### 15. What is a linking attack?

<details>
<summary>🤔 Click to reveal answer</summary>

An attack where an adversary combines the anonymized dataset with external data sources to re-identify individuals.

</details>

### 16. What is a homogeneity attack on k-anonymous data?

<details>
<summary>🤔 Click to reveal answer</summary>

When all records in an equivalence class have the same sensitive attribute value, allowing inference even without exact identification.

</details>

### 17. What was the Netflix Prize dataset attack?

<details>
<summary>🤔 Click to reveal answer</summary>

A famous de-anonymization attack where researchers linked "anonymous" Netflix ratings with public IMDb ratings to identify users.
### Practical Considerations

</details>

### 18. What factors should you consider when choosing k for k-anonymity?

<details>
<summary>🤔 Click to reveal answer</summary>

1) Sensitivity of data, 2) Risk tolerance, 3) Data utility requirements, 4) Size of dataset, 5) Regulatory requirements.

</details>

### 19. How do you balance privacy and data utility?

<details>
<summary>🤔 Click to reveal answer</summary>

1) Choose appropriate k value, 2) Use domain hierarchies for generalization, 3) Consider which attributes to generalize, 4) Evaluate information loss metrics.

</details>

### 20. What is the difference between anonymization and de-identification?

<details>
<summary>🤔 Click to reveal answer</summary>

De-identification removes direct identifiers but may still allow re-identification through quasi-identifiers. True anonymization makes re-identification practically impossible.
## 💡 Study Tips
- Practice k-anonymity transformations with sample datasets
- Understand the trade-offs between privacy and data utility
- Learn to identify quasi-identifiers in different contexts
- Study real-world privacy attack examples (Netflix, AOL search data)
- Practice calculating information loss metrics

</details>

---

📖 **[Return to Wiki Home](Home)**

🎯 **[Back to Examinator](https://github.com/QRY91/examinator)**