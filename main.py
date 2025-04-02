import requests
import csv
import xml.etree.ElementTree as ET

COMPANY_KEYWORDS = ["pharma", "biotech", "inc", "corp", "ltd"]

def fetch_papers(search_query):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        'db': 'pubmed',
        'term': search_query,
        'retmode': 'xml',
        'retmax': 100
    }
    
    try:
        print(f"Searching for: {search_query}")
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        root = ET.fromstring(response.text)
        id_list = root.find('IdList')
        papers = [pubmed_id.text for pubmed_id in id_list.findall('Id')]
        print(f"Debug: Found {len(papers)} papers.")
        return papers

    except requests.exceptions.RequestException as e:
        print(f"Error fetching papers: {e}")
        return []

def fetch_paper_details(pubmed_id):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {
        'db': 'pubmed',
        'id': pubmed_id,
        'retmode': 'xml'
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        root = ET.fromstring(response.text)
        doc_summary = root.find('DocSum')
        title = doc_summary.findtext("Item[@Name='Title']")
        pub_date = doc_summary.findtext("Item[@Name='PubDate']")
        authors = [item.text for item in doc_summary.findall("Item[@Name='AuthorList']/Item")]
        
        # Simulate extracting email and affiliation
        corresponding_author_email = "author@example.com"  # Placeholder
        company_affiliations = [author for author in authors if any(keyword in author.lower() for keyword in COMPANY_KEYWORDS)]
        
        return {
            'pubmed_id': pubmed_id,
            'title': title,
            'publication_date': pub_date,
            'non_academic_authors': ", ".join(company_affiliations),
            'corresponding_author_email': corresponding_author_email,
            'company_affiliations': ", ".join(company_affiliations)
        }
    except Exception as e:
        print(f"Error fetching details for paper {pubmed_id}: {e}")
        return None

def is_affiliated_with_company(details):
    if details and details['non_academic_authors']:
        return True
    return False

def save_to_csv(papers, filename):
    fieldnames = ['pubmed_id', 'title', 'publication_date', 'non_academic_authors', 'corresponding_author_email', 'company_affiliations']
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for paper in papers:
                writer.writerow(paper)
        print(f"Results saved to {filename}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def main():
    search_query = input("Enter search query: ").strip()
    if not search_query:
        print("Error: Search query cannot be empty.")
        return
    
    papers = fetch_papers(search_query)
    all_paper_details = []
    
    for pubmed_id in papers:
        print(f"Fetching details for paper {pubmed_id}...")
        details = fetch_paper_details(pubmed_id)
        if details and is_affiliated_with_company(details):
            all_paper_details.append(details)
    
    if all_paper_details:
        filename = input("Enter filename to save results (e.g., papers.csv): ").strip()
        save_to_csv(all_paper_details, filename)
    else:
        print("No papers matched the criteria.")

if __name__ == "__main__":
    main()
