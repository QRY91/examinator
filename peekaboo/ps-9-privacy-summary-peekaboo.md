# 🫣 Ps_9_Privacy_ Summary - Peekaboo Study Guide
*Generated from: ps_9_privacy_-summary.md*

**Click the details to reveal answers! Perfect for GitHub study sessions.**

---

# 🔒 Privacy & Data Protection - Clean Study Guide
## Privacy Fundamentals
**What is the difference between privacy and confidentiality?**
<details>
<summary>🤔 Click to reveal answer</summary>

Privacy is an individual's right to control how their personal data is used, while confidentiality is the obligation to keep information secret from unauthorized parties.

</details>

**What is personally identifiable information (PII)?**
<details>
<summary>🤔 Click to reveal answer</summary>

Any information that can be used to identify a specific individual, either directly (name, SSN) or indirectly when combined with other data.

</details>

**What are quasi-identifiers?**
<details>
<summary>🤔 Click to reveal answer</summary>

Attributes that alone don't uniquely identify someone, but when combined with other data sources can lead to re-identification (e.g., age, ZIP code, gender).

</details>

## GDPR (General Data Protection Regulation)
**What is the linking attack problem?**
<details>
<summary>🤔 Click to reveal answer</summary>

87% of the US population can be uniquely identified using just ZIP code, gender, and date of birth when combined with external datasets.

</details>

**What are the main principles of GDPR?**
<details>
<summary>🤔 Click to reveal answer</summary>

1) Lawful, fair, transparent processing, 2) Purpose limitation, 3) Data minimization, 4) Accuracy, 5) Storage limitation, 6) Integrity & confidentiality, 7) Accountability.

</details>

**What is data minimization under GDPR?**
<details>
<summary>🤔 Click to reveal answer</summary>

Only collecting personal data that is necessary and relevant for the specific, stated purpose - no more than required.

</details>

**What are the key individual rights under GDPR?**
<details>
<summary>🤔 Click to reveal answer</summary>

Right to access, right to rectification, right to erasure (right to be forgotten), right to data portability, right to object.

</details>

**What is the right to be forgotten?**
<details>
<summary>🤔 Click to reveal answer</summary>

Individuals can request organizations to delete their personal data under certain circumstances, such as when data is no longer necessary.

</details>

## Data Anonymization Techniques
**Who is responsible for GDPR compliance?**
<details>
<summary>🤔 Click to reveal answer</summary>

The data controller (who determines purposes and means of processing) bears primary responsibility for compliance.

</details>

**What is data anonymization?**
<details>
<summary>🤔 Click to reveal answer</summary>

The process of removing or altering personally identifiable information so that individuals cannot be identified from the dataset.

</details>

**What are the main anonymization techniques?**
<details>
<summary>🤔 Click to reveal answer</summary>

1) Blanking (removing data), 2) Hashing (one-way transformation), 3) Masking (partial obscuring), 4) Generalization (making data less specific), 5) Suppression (removing records).

</details>

**What is generalization in data anonymization?**
<details>
<summary>🤔 Click to reveal answer</summary>

Replacing specific values with more general ones (e.g., exact age "25" becomes age range "20-30").

</details>

## K-Anonymity
**What is suppression in data anonymization?**
<details>
<summary>🤔 Click to reveal answer</summary>

Removing entire records or fields that contain unique or sensitive information that cannot be generalized.

</details>

**What is k-anonymity?**
<details>
<summary>🤔 Click to reveal answer</summary>

A privacy preservation technique ensuring that each record in a dataset is indistinguishable from at least k-1 other records based on quasi-identifiers.

</details>

**What does k=3 anonymity mean?**
<details>
<summary>🤔 Click to reveal answer</summary>

Every combination of quasi-identifier values appears at least 3 times in the dataset, so any individual is indistinguishable from at least 2 others.

</details>

**How do you achieve k-anonymity?**
<details>
<summary>🤔 Click to reveal answer</summary>

Through generalization (making values less specific) and suppression (removing outlier records) of quasi-identifiers.

</details>

## Privacy Attacks
**What are the limitations of k-anonymity?**
<details>
<summary>🤔 Click to reveal answer</summary>

1) Homogeneity attack (if all k records have same sensitive value), 2) Background knowledge attack, 3) Data utility loss through generalization.

</details>

**What is a homogeneity attack on k-anonymous data?**
<details>
<summary>🤔 Click to reveal answer</summary>

When all records in an equivalence class have the same sensitive attribute value, allowing inference even without exact identification.

</details>

**What was the Netflix Prize dataset attack?**
<details>
<summary>🤔 Click to reveal answer</summary>

A famous de-anonymization attack where researchers linked "anonymous" Netflix ratings with public IMDb ratings to identify users.

</details>

**What is a linking attack?**
<details>
<summary>🤔 Click to reveal answer</summary>

Combining an anonymized dataset with external data sources to re-identify individuals using quasi-identifiers.

</details>

## Advanced Privacy Techniques
**What is background knowledge attack?**
<details>
<summary>🤔 Click to reveal answer</summary>

Using additional information about individuals (not in the dataset) to reduce anonymity and potentially identify people.

</details>

**What is l-diversity?**
<details>
<summary>🤔 Click to reveal answer</summary>

An extension of k-anonymity that ensures each equivalence class has at least l different values for sensitive attributes, preventing homogeneity attacks.

</details>

**What is t-closeness?**
<details>
<summary>🤔 Click to reveal answer</summary>

Further refinement requiring that the distribution of sensitive attributes in each equivalence class is close to the overall distribution.

</details>

**What is differential privacy?**
<details>
<summary>🤔 Click to reveal answer</summary>

A privacy technique that adds carefully calibrated random noise to query results, providing mathematical guarantees about privacy.

</details>

## Practical Privacy Implementation
**What are the advantages of differential privacy?**
<details>
<summary>🤔 Click to reveal answer</summary>

1) Mathematical privacy guarantees, 2) Composability (multiple queries), 3) Resistance to auxiliary information attacks, 4) Better utility preservation.

</details>

**When is personal data considered truly anonymized under GDPR?**
<details>
<summary>🤔 Click to reveal answer</summary>

When data is irreversibly altered so that individuals cannot be identified directly or indirectly, even with additional information.

</details>

**What is pseudonymization?**
<details>
<summary>🤔 Click to reveal answer</summary>

Replacing identifying information with artificial identifiers while maintaining a separate mapping that can be reversed if needed.

</details>

**What factors should you consider when choosing k for k-anonymity?**
<details>
<summary>🤔 Click to reveal answer</summary>

1) Sensitivity of data, 2) Risk tolerance, 3) Data utility requirements, 4) Size of dataset, 5) Regulatory requirements.

</details>

## Database Privacy
**How do you balance privacy and data utility?**
<details>
<summary>🤔 Click to reveal answer</summary>

1) Choose appropriate anonymization level, 2) Use domain hierarchies for generalization, 3) Consider which attributes to generalize, 4) Evaluate information loss metrics.

</details>

**What is database sanitization?**
<details>
<summary>🤔 Click to reveal answer</summary>

Removing or protecting private information from databases before sharing or analysis to prevent privacy breaches.

</details>

**What is SQL sanitization for privacy?**
<details>
<summary>🤔 Click to reveal answer</summary>

Techniques to prevent SQL injection attacks that could lead to unauthorized access to personal data in databases.

</details>

**Why is data retention important for privacy?**
<details>
<summary>🤔 Click to reveal answer</summary>

Keeping personal data longer than necessary increases privacy risks and may violate regulations like GDPR's storage limitation principle.

</details>
