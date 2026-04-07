# Disbursement Queries 
import os
from pathlib import Path

def do_disb_queries(test, date, year, query, renamed, renamed_disb):

    aid_year = str(int(year) - 1) + "-" + str(year)
    month_folder = date[:2] + "-20" + date[-2:]

    if test:
        directory = os.path.realpath(os.path.join('C:/Testing Bob/Disbursement', aid_year, month_folder))
        pell_directory = os.path.realpath(os.path.join('C:/Testing Bob/Pell Reports', aid_year, month_folder))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/Disbursement', aid_year, month_folder))
        pell_directory = os.path.realpath(os.path.join('O:/Systems/Pell Reports', aid_year, month_folder))

    if not os.path.isdir(directory):
        os.makedirs(directory)
    if not os.path.isdir(pell_directory):
        os.makedirs(pell_directory)

    move_directory = "Daily Reports"
    move_pell_directory = "Pell Reports"
    
    if query.startswith("UUFA_DQ_AUTHORIZED_NOT_DISB"):
        return (query, renamed_disb, directory, move_directory)

    if query.startswith("UUFA_DQ_ALL_DISBURSED"):
        return (query, renamed_disb, directory, move_directory)

    if query.startswith("FA_DQ_ATHLETE_RM_BD"):
        return (query, renamed_disb, directory, move_directory)

    if query.startswith("FA_DQ_ATH_OFF_SCHED_RM_BD"):
        return (query, renamed_disb, directory, move_directory)

    if ("_CASH_DISB_TOTALS") in query:
        return (query, renamed_disb, directory, move_directory)

    if ("_DQ_DISB_TOTALS") in query:
        return (query, renamed_disb, directory, move_directory)

    if query.startswith("UUFA_DQ_FALL") :
        return (query, renamed_disb, directory, move_directory)

    if query.startswith("UUFA_DQ_FALL_SPRING"):
        return (query, renamed_disb, directory, move_directory)

    if query.startswith("UUFA_DQ_DL_SUMMER"):
        return (query, renamed_disb, directory, move_directory)

    if query.startswith("UUFA_DQ_SPRING"):
        return (query, renamed_disb, directory, move_directory)

    if query.startswith("UUFA_DQ_UG_PLUS_REFUND_IA"):
        return (query, renamed_disb, directory, move_directory)

    if ("DQ_MISC_CARES_DISB") in query:
        return (query, renamed_disb, directory, move_directory)

    if ("DQ_MISC_CARES_RES_DISB") in query:
        return (query, renamed_disb, directory, move_directory)

    if ("MISC_DISB_TOTALS") in query:
        return (query, renamed_disb, directory, move_directory)

    if query.startswith("UUFA_DQ_MISC_RESOURCE_DISB"):
        return (query, renamed_disb, directory, move_directory)

    if ("NONCASH_DISB_TOTALS") in query:
        return (query, renamed_disb, directory, move_directory)

    if query.startswith("UUFA_DQ_PELL_ACPT_GR8_DISB"):
        return (query, renamed_disb, directory, move_directory)

    if query.startswith("UUFA_DQ_SF_ITEM_TYPE_ERROR"):
        return (query, renamed_disb, directory, move_directory)

    if query.startswith("UUFA_DQ_TEACH_GRANT"):
        return (query, renamed_disb, directory, move_directory)

    if query.startswith("UUFA_DQ_DISB_BREAKDOWN") :
        return (query, renamed_disb, directory, move_directory)

    if ("_DQ_DISB_TOTALS") in query :
        return (query, renamed_disb, directory, move_directory)
    
    if query.startswith("UUFA_DQ_FALL") and "SPRING" not in query:
        return (query, renamed_disb, directory, move_directory)

    if query.startswith("UUFA_DQ_PELL_ACPT_GR8_DISB") :
        return (query, renamed_disb, directory, move_directory)

    if "UUFA_PELL_AID_APPL_STATUS" in query :
        return (query, renamed, pell_directory, move_pell_directory)

    if "UUFA_PELL_COD_DISB_DETAIL" in query :
        return (query, renamed, pell_directory, move_pell_directory)

    if "UUFA_PELL_COD_DISB_ENTRY" in query :
        return (query, renamed, pell_directory, move_pell_directory)

    if "UUFA_PELL_COD_FYTD_AMOUNTS" in query :
        return (query, renamed, pell_directory, move_pell_directory)

    if "UUFA_PELL_COD_PHOLD_RJCTD" in query :
        return (query, renamed, pell_directory, move_pell_directory)

    if "UUFA_PELL_COA_BLANK" in query :
        return (query, renamed, pell_directory, move_pell_directory)

    if "UUFA_PELL_PRCSS_STAT_BLNK" in query :
        return (query, renamed, pell_directory, move_pell_directory)

    if "UUFA_PELL_RSP_COD_EDITS" in query :
        return (query, renamed, pell_directory, move_pell_directory)

    if "UUFA_PELL_RSP_COD_IN" in query :
        return (query, renamed, pell_directory, move_pell_directory)

    if "UUFA_PELL_RSP_DISB_ACTION_CODE" in query :
        return (query, renamed, pell_directory, move_pell_directory)

    if "UUFA_PELL_RSP_ORIG_AWARD" in query :
        return (query, renamed, pell_directory, move_pell_directory)

    return "Empty" #Leave as last line

