# Alt Loan Pre-Outbound Queries
import os   

def al_pre_outbound(test, query, renamed):

    if test:
        directory = os.path.realpath('C:/Testing Bob/ALT Loans/')
    else:
        directory = os.path.realpath('O:/Systems/QUERIES/ALT Loans/')

    if not os.path.isdir(directory):
        os.makedirs(directory)

    move_directory = "Alternative Loan Reports"

    # FORMAT: return (query, renamed, archive_directory, UOSFA_folder)
    # query: The original file name
    # renamed: The name the file should have after being moved
    # archive_directory: The folder the file will be copied to
    # UOSFA_folder: The name of the folder the renamed file should be moved to
    # - (eg. "Budget Reports", "SAP Reports", "Unknown Reports") 
    # - put "None" if it shouldn't be moved to a folder in 'O:/UOSFA Reports/'

    if query.startswith("UUFA_ALR_110_CHNG_PDG_TRANS"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_CL_APP_RSPNS_ERR"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALT_LN_AWRD_DISC"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALT_LN_NO_DISB"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LN_SENT_NO_RESP"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LN_EFT_DETAIL_ERR"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LN_EFT_DT_LNDR_ERR"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LOAN_ORIG_ACAD_LVL"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LN_ORIG_EDIT_ERR"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LOAN_ORIG_FA_LOAD"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LOAN_ORG_LND_NT_CK"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LOAN_ORIG_SPLT_CDS"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LN_ORIG_VLOAN_RSN"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LOAN_SPC_NEED_OVWD"):
        return (query, renamed, directory, move_directory)
    
    if query.startswith("UUFA_ALT_LOANS_RECIEVED_NO_SSN"):
        return (query, renamed, directory, move_directory)
    
    if query.startswith("UUFA_ALT_LOANS_SSN_MATCH"):
        return (query, renamed, directory, move_directory)
    
    if query.startswith("UUFA_ALT_LN_AWRD_DISC"):
        return (query, renamed, directory, move_directory)
    
    if query.startswith("UUFA_ALT_LN_NO_DISB"):
        return (query, renamed, directory, move_directory)

    return "Empty" #Leave as final line
    