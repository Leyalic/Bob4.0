# Direct Loan Pre-Outbound Queries
import os   

def dl_pre_outbound(test, date, year, query, renamed):

    if test:
        directory = os.path.realpath(os.path.join('C:/Testing Bob/Direct Loans', 'DL Pre-Outbound'))
        heal_directory = os.path.realpath(os.path.join('C:/Testing Bob/Direct Loans', 'DL HEAL Flag'))
        response_directory = os.path.realpath(os.path.join('C:/Testing Bob/Direct Loans', 'DL Response Files'))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/Direct Loans', 'DL Pre-Outbound'))
        heal_directory = os.path.realpath(os.path.join('O:/Systems/Direct Loans', 'DL HEAL Flag'))
        response_directory = os.path.realpath(os.path.join('O:/Systems/Direct Loans', 'DL Response Files'))
       
    if not os.path.isdir(directory):
        os.makedirs(directory)
    if not os.path.isdir(heal_directory):
        os.makedirs(heal_directory)
    if not os.path.isdir(response_directory):
        os.makedirs(response_directory)

    move_directory = "Direct Loan Reports"
    other_directory = "Other Reports"

    # FORMAT: return (query, renamed, archive_directory, UOSFA_folder)
    # query: The original file name
    # renamed: The name the file should have after being moved
    # archive_directory: The folder the file will be copied to
    # UOSFA_folder: The name of the folder the renamed file should be moved to
    # - (eg. "Budget Reports", "SAP Reports", "Unknown Reports") 
    # - put "None" if it shouldn't be moved to a folder in 'O:/UOSFA Reports/'

    if query.startswith("UUFA_DL_COD_EDITS"):
        return (query, renamed, response_directory, move_directory)

    if query.startswith("UUFA_DLO_PRORATION_ENROLL"):
        return (query, renamed, heal_directory, move_directory)

    if query.startswith("UUFA_DLR_ORIG_TRNS_PEND"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_ENTRANCE_COUNSEL"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_LOAN_EFT_DT_LNDR_ERR"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_LOAN_ORIG_FA_LOAD"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_LOAN_NO_NSLDS"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_LOAN_ORIG_ACAD_LVL"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_LOAN_ORIG_EDIT_ERR"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_LOAN_ORIG_SPLT_CDS"):
        return (query, renamed, directory, move_directory)
    
    if "DLR_LN_ORIG_VLOAN_RSN" in query:
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_LOAN_SPC_NEED_OVWD"):
        return (query, renamed, directory, move_directory)

    if "DLR_LN_ACPT_STAF_31_32" in query:
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_NOT_DISB"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_NOT_DISBURSED"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_NOT_DISBURSED_20"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_UG_PLUS_REFND_IND"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ADJUST_LOAN_DATES"):
        return (query, renamed, directory, other_directory)
    
    if query.startswith("UUFA_IL_RPKG_DL_OFFERS"):
        return (query, renamed, directory, other_directory)
    
    return "Empty" #Leave as final line
