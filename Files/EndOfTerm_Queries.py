# End of Term Queries
import os

def do_end_of_term_queries(test, date, year, query, renamed):

    if test:
        directory = os.path.realpath(os.path.join('C:/Testing Bob/SAP/', year))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/SAP/', year))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    move_directory = "SAP Reports"

    # For underscores - to be removed/commented when the SAP process is automated
    dot_index = query.rfind(".")
    right_index = query.rfind("_")
    renamed = date + " " + query[:right_index] + " " + year[2:] + query[dot_index:]

    # FORMAT: return (query, renamed, archive_directory, UOSFA_folder)
    # query: The original file name
    # renamed: The name the file should have after being moved
    # archive_directory: The folder the file will be copied to
    # UOSFA_folder: The name of the folder the renamed file should be moved to
    # - (eg. "Budget Reports", "SAP Reports", "Unknown Reports") 
    # - put "None" if it shouldn't be moved to a folder in 'O:/UOSFA Reports/'

    if query.startswith("UUFA_EOT_SAP_AGGCP_DLM"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_ACAD_PLAN_RVW_FRAP"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_CBA_ACAD_PRG_BELOW_FT"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_CBA_UNDISBURSED"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_ALT_LOAN_SAP"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_LN_ORIG_FAIL_PENDING"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_LN_ACD_PRG_BLW_HT_UND"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_LN_ACD_PRG_BLW_HT_SUB"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_PRO_STDNT_SAP_WARNING"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_MED_SAP"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_FWS_WITH_NSI_HOLD"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_PELL_ACD_PRG_LES_THN"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_PELL_OFFERED_NOT_DIS"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_THESIS_STUDENT_NONRES"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_SCH_ACAD_PROG_REVIEW"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_SCH_ACD_PRG_REVIEW"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_SAP_AGGCP_DENTAL"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_SAP_AGGCP_LAW"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_SAP_AGGCP_MED"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_EU_FALL_GRADE"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_EU_SPRING_GRADE"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_EU_SUMMER_GRADE"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_PELL_ELG_ENRLL_NO_AWD"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_SAP_FSAP"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_EOT_SCHOLAR_LEADER_CGPA"):
        return (query, renamed, directory, move_directory)

    if "EOT_WUE_ACAD_PROG_REV" in query:
        return (query, renamed, directory, move_directory)             

    return "Empty" #Leave as last line
