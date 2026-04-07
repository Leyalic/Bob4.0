# After Repackaging Queries 
import os

def do_after_repackaging(test, year, query, renamed):

    aid_year = str(int(year) - 1) + "-" + str(year)

    if test:
        directory = os.path.realpath(os.path.join('C:/Testing Bob/Pell Repackaging', aid_year))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/Pell Repackaging', aid_year))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    move_directory = "Pell Reports"

    # FORMAT: return (query, renamed, archive_directory, UOSFA_folder)
    # query: The original file name
    # renamed: The name the file should have after being moved
    # archive_directory: The folder the file will be copied to
    # UOSFA_folder: The name of the folder the renamed file should be moved to
    # - (eg. "Budget Reports", "SAP Reports", "Unknown Reports") 
    # - put "None" if it shouldn't be moved to a folder in 'O:/UOSFA Reports/'

    if query.startswith("UUFA_AP_RPKG_5TH_YR_2ND_BACH"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_AP_RPKG_ACTN"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_AP_RPKG_AWACT_C"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_AP_RPKG_AW_ACT"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_AP_RPKG_FPEL_AWARD_LCK"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_AP_RPKG_PLAN_ID_BLANK"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_AP_RPKG_RPKG_SNAPSHOT"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_AP_RPKG_SAP_HOLD_DELETED"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_AP_RPKG_SKIP"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_AP_RPKG_TERM_FT"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_AP_RPKG_TERM_HT"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_AP_RPKG_TERM_LH"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_AP_RPKG_TERM_NL"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_AP_RPKG_TERM_TQ"):
        return (query, renamed, directory, move_directory)

    return "Empty" #Leave as last line