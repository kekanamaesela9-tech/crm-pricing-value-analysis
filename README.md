# CRM Pricing and Perceived Value Analysis

## Overview
This project analyzes how pricing relates to perceived value and adoption risk across CRM software products. It demonstrates end-to-end analytical work using real-world, unstructured review data, with a focus on defensible assumptions and business relevance rather than data volume.

The project covers data collection, cleaning, feature engineering, comparative analysis, and insight generation.

---

## Business Question
How does CRM pricing relate to perceived value and customer adoption risk across products?

Perceived value is assessed using:
- User ratings as a proxy for product quality
- Review volume as a proxy for adoption and retention

---

## Data

### Data Source
Data was collected from Capterra, a public software review platform. Product-level information was extracted directly from individual CRM product pages.

### Products Included
The final analysis includes the following CRM tools:
- Salesforce Sales Cloud
- HubSpot CRM
- Monday CRM
- Microsoft Dynamics 365 Sales
- Kylas Sales CRM

Products with incompatible or inconsistent page structures were excluded to preserve pipeline stability.

---

## Methodology

### Data Collection
Initial attempts to collect data using standard HTTP requests resulted in access restrictions. Selenium was therefore used to extract dynamically rendered content. The data collection pipeline was designed to log failures and continue execution rather than crash, reflecting real-world data constraints.

### Data Cleaning and Feature Engineering
Unstructured pricing text was parsed and transformed into numeric features:
- **min_price**: lowest available pricing tier
- **max_price**: highest paid pricing tier

Pricing logic explicitly accounted for:
- Free tiers
- Paid tiers
- Mixed pricing models

Missing or ambiguous pricing values were left as null to avoid introducing false precision.

### Value Metric Design
A custom value metric was created to balance perceived quality and adoption:
value_score = rating * log(review_count)

- Rating represents perceived quality
- Review count represents adoption and trust
- Log scaling reduces skew from very large products

This metric enables meaningful comparison across tools of different sizes.

---

## Analysis

### Comparative Ranking
Products were ranked by value_score to identify which tools deliver the highest perceived value relative to their market presence.

### Visualization
A price versus perceived value scatter plot was created to visualize:
- Pricing tiers
- Value concentration
- Differences in market positioning

Each product was labeled directly to improve interpretability.

---

## Key Insights
- Higher pricing does not automatically correspond to higher perceived value.
- Products with strong adoption can achieve high value scores even at mid-range price points.
- Free entry tiers reduce adoption friction but do not guarantee long-term value without effective conversion.
- Premium pricing is most defensible when supported by scale and trust rather than marginal rating differences.

---

## Business Implications
- Premium CRM vendors should actively protect review sentiment and adoption signals, as perceived value is highly sensitive to trust indicators.
- Mid-priced tools should prioritize differentiation and specialization rather than competing solely on price.
- Free-tier strategies should focus on conversion paths to sustain long-term value.

---

## Limitations
- Review count is used as a proxy for adoption and retention and does not directly measure churn.
- Pricing reflects publicly listed plans and may not capture negotiated enterprise contracts.
- The analysis is comparative and directional rather than causal.

---

## Tools Used
- Python
- pandas
- matplotlib
- Selenium
- Regular expressions


