# PubMed-Fetch-Research-Papers
# Research Paper Fetching Tool

## Overview
This project involves the development of a Python-based tool to fetch research papers from PubMed using its API. The tool filters papers with at least one author affiliated with a pharmaceutical or biotech company and saves the results in a CSV file. The goal is to streamline the process of identifying relevant scientific articles for industry-related research.

## Objective
- Enable users to search PubMed for research papers using a keyword-based query.
- Identify papers authored by professionals affiliated with pharmaceutical or biotech companies.
- Output the filtered results in a user-friendly format, such as a CSV file.

## Approach
### 1. Input Handling
- The user is prompted to enter a search query.
- The input is validated to ensure it is non-empty.

### 2. PubMed API Integration
- **Esearch API**: Used to fetch PubMed IDs corresponding to the search query.
- **Esummary API**: Used to retrieve details (e.g., title, publication date, author affiliations) for each PubMed ID in batches.

### 3. Filtering Criteria
- Authors affiliated with organizations containing specific keywords (e.g., "pharma," "biotech," "labs") are identified.
- Only papers with at least one such author are retained.

### 4. Data Output
- The filtered results are saved in a CSV file with the following columns:
  - `pubmed_id`
  - `title`
  - `publication_date`
  - `company_affiliations`

## Methodology
### Step 1: Fetching PubMed IDs
- The `fetch_papers` function queries PubMed using the Esearch API.
- The function returns a list of PubMed IDs for papers matching the query.

### Step 2: Retrieving Paper Details
- The `fetch_paper_details_batch` function uses the Esummary API to fetch details for batches of PubMed IDs.
- Author affiliations are analyzed to identify potential company links based on predefined keywords.

### Step 3: Saving Results
- The `save_to_csv` function writes the filtered paper details to a CSV file.
- The CSV includes the specified columns, ensuring clarity and accessibility of the data.

### Step 4: Error Handling and Rate Limits
- Network errors and API rate limits are handled with retries and delays.
- Graceful error messages are displayed for user awareness.

## Results
### Key Outputs
- Papers matching the search query are fetched successfully.
- Papers with at least one company-affiliated author are filtered and saved.
- CSV file (`output.csv`) includes:
  - Titles, PubMed IDs, publication dates, and company affiliations.

### Sample CSV Format
| pubmed_id | title | publication_date | company_affiliations |
|-----------|--------------------------------|----------------|---------------------|
| 37907989 | AI in Drug Discovery | 2025-01-05 | PharmaCorp, Biotech Ltd |
| 33401123 | Neural Networks in Medicine | 2024-12-15 | TechLabs Inc |
| 28389682 | Machine Learning for Drug Design | 2024-10-10 | R&D Solutions |

### Console Output
```
Enter search query: artificial intelligence
Fetching papers for query: artificial intelligence
Found 100 papers.
Fetching details for batch: ['37907989', '33401123', '28389682', ...]
Fetching details for paper 37907989...
Fetching details for paper 33401123...
Fetching details for paper 28389682...
Results saved to output.csv
```

## Strengths
1. **Ease of Use**: Simple console-based interaction.
2. **Efficient Filtering**: Targets company-affiliated authors based on relevant keywords.
3. **Scalable**: Batch processing supports large datasets.
4. **Error Resilience**: Handles API rate limits and network errors gracefully.
5. **Output Quality**: CSV format ensures the data is organized and accessible.

## Challenges and Limitations
1. **Keyword-Based Filtering**: The approach may miss affiliations not containing predefined keywords.
2. **Rate Limit Delays**: Prolonged execution time when many requests hit rate limits.
3. **Limited Query Scope**: The Esearch API restricts the maximum number of results per query to 100.
4. **No Advanced Analysis**: The tool doesn’t analyze paper content, only metadata.

## Future Enhancements
1. **Advanced Affiliation Parsing**
   - Use natural language processing (NLP) to identify company affiliations more accurately.
2. **User Interface**
   - Develop a graphical user interface (GUI) for better usability.
3. **Query Optimization**
   - Allow users to specify additional parameters (e.g., publication date range).
4. **Data Analysis**
   - Include statistics on the number of papers per company or industry sector.
5. **File Format Options**
   - Offer output in formats like JSON or Excel in addition to CSV.

## Conclusion
The Research Paper Fetching Tool provides an efficient and user-friendly solution for retrieving and filtering PubMed articles based on user queries and author affiliations. While it currently focuses on a straightforward use case, the tool lays a strong foundation for more advanced features and analytical capabilities in the future.
