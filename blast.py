"""
This module is the result of the Colorifix task assignment and contains functions that perform the following functions:
    - Compute BLAST operations against the NCBI server, mediated by the BioPython libraries
    - Count the number of hits obtained from a BLAST operation for a given nucleotide sequence

If run as a main module, the specific conditions for this exercise will be run, as stated under if __name__ == "__main__"
"""

from Bio.Blast import NCBIWWW
from bs4 import BeautifulSoup as bsoup


def count_hits(blast_xml):
    """
    This function counts the number of hits from an XML structure containing BLAST query results
    Arguments:
        blast_xml -- a string containing the XML structure for the BLAST query result

    Returns:
        n_hits -- the number of hits contained in the BLAST XML structure
    """

    # Create a Beautiful Soup object to parse the XML content
    soup = bsoup(blast_xml, "xml")

    # Retrieve the Iteration_hits tag from the XML structure
    iter_hits = soup.Iteration_hits

    # Each BLAST Hit is stored as a children tag in <Iteration_hits>
    # Iterate <Iteration_hits> to count the number of hits
    n_hits = 0
    for hit in iter_hits:
        if hit != "\n":
            n_hits += 1

    return n_hits


def run_blast(sequence, program, database):
    """
    Runs a BLAST operation against the NCBI server
    Arguments:
        sequence -- a string containing the nucleotide sequence to be aligned
        program -- a string containing the BLAST program algorithm to be used
        database -- a string defining the database against which the BLAST is performed

    Returns:
        blast_result -- a string containing the XML structure with the BLAST results
    """
    handle = NCBIWWW.qblast(program, database, sequence)
    blast_xml = handle.read()

    return blast_xml


if __name__ == "__main__":
    # Define parameters for the BLAST exercise
    sequence = "ATGTGGGTGATAGGATGGGTCGACTGACTAGCATCGATCGACTAGCTAGCATCGATC"
    program = "blastn"
    database = "nr"

    # Run BLAST for the defined parameters
    blast_result = run_blast(sequence, program, database)

    # Compute the number of BLAST hits for the given nucleotide sequence
    n_hits = count_hits(blast_result)
    print("Number of hits: {}".format(n_hits))
