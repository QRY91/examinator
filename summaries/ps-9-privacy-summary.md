# 🔒 Privacy & Data Protection - Clean Study Guide

## Privacy Fundamentals

**Q: What is the difference between privacy and confidentiality?**
A: Privacy is an individual's right to control how their personal data is used, while confidentiality is the obligation to keep information secret from unauthorized parties.

**Q: What is personally identifiable information (PII)?**
A: Any information that can be used to identify a specific individual, either directly (name, SSN) or indirectly when combined with other data.

**Q: What are quasi-identifiers?**
A: Attributes that alone don't uniquely identify someone, but when combined with other data sources can lead to re-identification (e.g., age, ZIP code, gender).

**Q: What is the linking attack problem?**
A: 87% of the US population can be uniquely identified using just ZIP code, gender, and date of birth when combined with external datasets.

## GDPR (General Data Protection Regulation)

**Q: What are the main principles of GDPR?**
A: 1) Lawful, fair, transparent processing, 2) Purpose limitation, 3) Data minimization, 4) Accuracy, 5) Storage limitation, 6) Integrity & confidentiality, 7) Accountability.

**Q: What is data minimization under GDPR?**
A: Only collecting personal data that is necessary and relevant for the specific, stated purpose - no more than required.

**Q: What are the key individual rights under GDPR?**
A: Right to access, right to rectification, right to erasure (right to be forgotten), right to data portability, right to object.

**Q: What is the right to be forgotten?**
A: Individuals can request organizations to delete their personal data under certain circumstances, such as when data is no longer necessary.

**Q: Who is responsible for GDPR compliance?**
A: The data controller (who determines purposes and means of processing) bears primary responsibility for compliance.

## Data Anonymization Techniques

**Q: What is data anonymization?**
A: The process of removing or altering personally identifiable information so that individuals cannot be identified from the dataset.

**Q: What are the main anonymization techniques?**
A: 1) Blanking (removing data), 2) Hashing (one-way transformation), 3) Masking (partial obscuring), 4) Generalization (making data less specific), 5) Suppression (removing records).

**Q: What is generalization in data anonymization?**
A: Replacing specific values with more general ones (e.g., exact age "25" becomes age range "20-30").

**Q: What is suppression in data anonymization?**
A: Removing entire records or fields that contain unique or sensitive information that cannot be generalized.

## K-Anonymity

**Q: What is k-anonymity?**
A: A privacy preservation technique ensuring that each record in a dataset is indistinguishable from at least k-1 other records based on quasi-identifiers.

**Q: What does k=3 anonymity mean?**
A: Every combination of quasi-identifier values appears at least 3 times in the dataset, so any individual is indistinguishable from at least 2 others.

**Q: How do you achieve k-anonymity?**
A: Through generalization (making values less specific) and suppression (removing outlier records) of quasi-identifiers.

**Q: What are the limitations of k-anonymity?**
A: 1) Homogeneity attack (if all k records have same sensitive value), 2) Background knowledge attack, 3) Data utility loss through generalization.

## Privacy Attacks

**Q: What is a homogeneity attack on k-anonymous data?**
A: When all records in an equivalence class have the same sensitive attribute value, allowing inference even without exact identification.

**Q: What was the Netflix Prize dataset attack?**
A: A famous de-anonymization attack where researchers linked "anonymous" Netflix ratings with public IMDb ratings to identify users.

**Q: What is a linking attack?**
A: Combining an anonymized dataset with external data sources to re-identify individuals using quasi-identifiers.

**Q: What is background knowledge attack?**
A: Using additional information about individuals (not in the dataset) to reduce anonymity and potentially identify people.

## Advanced Privacy Techniques

**Q: What is l-diversity?**
A: An extension of k-anonymity that ensures each equivalence class has at least l different values for sensitive attributes, preventing homogeneity attacks.

**Q: What is t-closeness?**
A: Further refinement requiring that the distribution of sensitive attributes in each equivalence class is close to the overall distribution.

**Q: What is differential privacy?**
A: A privacy technique that adds carefully calibrated random noise to query results, providing mathematical guarantees about privacy.

**Q: What are the advantages of differential privacy?**
A: 1) Mathematical privacy guarantees, 2) Composability (multiple queries), 3) Resistance to auxiliary information attacks, 4) Better utility preservation.

## Practical Privacy Implementation

**Q: When is personal data considered truly anonymized under GDPR?**
A: When data is irreversibly altered so that individuals cannot be identified directly or indirectly, even with additional information.

**Q: What is pseudonymization?**
A: Replacing identifying information with artificial identifiers while maintaining a separate mapping that can be reversed if needed.

**Q: What factors should you consider when choosing k for k-anonymity?**
A: 1) Sensitivity of data, 2) Risk tolerance, 3) Data utility requirements, 4) Size of dataset, 5) Regulatory requirements.

**Q: How do you balance privacy and data utility?**
A: 1) Choose appropriate anonymization level, 2) Use domain hierarchies for generalization, 3) Consider which attributes to generalize, 4) Evaluate information loss metrics.

## Database Privacy

**Q: What is database sanitization?**
A: Removing or protecting private information from databases before sharing or analysis to prevent privacy breaches.

**Q: What is SQL sanitization for privacy?**
A: Techniques to prevent SQL injection attacks that could lead to unauthorized access to personal data in databases.

**Q: Why is data retention important for privacy?**
A: Keeping personal data longer than necessary increases privacy risks and may violate regulations like GDPR's storage limitation principle.
