# ATB, FBILL, 3C Queries
import os

def do_atb_fb_3c_queries(test, query, renamed):

    if test:
        directory = os.path.realpath(os.path.join('C:/Testing Bob/QUERIES/3C Queries'))
        atb_directory = os.path.realpath(os.path.join('C:/Testing Bob/QUERIES/ATB'))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/3C Queries'))
        atb_directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/ATB'))

    if not os.path.isdir(directory):
        os.makedirs(directory)
    if not os.path.isdir(atb_directory):
        os.makedirs(atb_directory)

    move_directory = "Daily Reports"
    atb_move_directory = "Daily Reports"

    # FORMAT: return (query, renamed, archive_directory, UOSFA_folder)
    # query: The original file name
    # renamed: The name the file should have after being moved
    # archive_directory: The folder the file will be copied to
    # UOSFA_folder: The name of the folder the renamed file should be moved to
    # - (eg. "Budget Reports", "SAP Reports", "Unknown Reports") 
    # - put "None" if it shouldn't be moved to a folder in 'O:/UOSFA Reports/'

    if ("UUFA_ADD_FDLP" in query):
        return (query, renamed, directory, move_directory)

    if ("UUFA_ADD_FGLO" in query):
        return (query, renamed, directory, move_directory)

    if ("UUFA_ADD_FHST" in query):
        return (query, renamed, directory, move_directory)

    if ("UUFA_ADD_FMPN" in query):
        return (query, renamed, directory, move_directory)

    if ("UUFA_ADD_FNON" in query):
        return (query, renamed, directory, move_directory)

    if ("UUFA_ADD_FTYN" in query):
        return (query, renamed, directory, move_directory)

    if ("UUFA_ADD_FULO" in query):
        return (query, renamed, directory, move_directory)

    if ("UUFA_ADD_FLPR" in query):
        return (query, renamed, directory, move_directory)

    if ("UUFA_COMPLETE_FDLP" in query):
        return (query, renamed, directory, move_directory)

    if ("UUFA_COMPLETE_FGLO" in query):
        return (query, renamed, directory, move_directory)

    if ("UUFA_COMPLETE_FHST" in query):
        return (query, renamed, directory, move_directory)

    if ("UUFA_COMPLETE_FMPN" in query):
        return (query, renamed, directory, move_directory)

    if ("UUFA_COMPLETE_FNON" in query) :
        return (query, renamed, directory, move_directory)

    if ("UUFA_COMPLETE_FULO" in query):
        return (query, renamed, directory, move_directory)

    if ("UUFA_HS_06_AFTER_ATB" in query):
        return (query, renamed, atb_directory, atb_move_directory)

    if ("UUFA_HS_04_AFTER_ATB" in query):
        return (query, renamed, atb_directory, atb_move_directory)

    if ("UUFA_GED_07_AFTER_ATB" in query):
        return (query, renamed, atb_directory, atb_move_directory)

    if ("UUFA_GED_07_AFTER_SEC" in query):
        return (query, renamed, atb_directory, atb_move_directory)

    if ("UUFA_HS_04_AFTER_SEC" in query):
        return (query, renamed, atb_directory, atb_move_directory)
    
    if ("UUFA_HS_06_AFTER_SEC" in query):
        return (query, renamed, atb_directory, atb_move_directory)

    if ("UUFA_ATB_ISIR_NOT_MATCH" in query):
        return (query, renamed, atb_directory, atb_move_directory)

    if ("UUFA_ATB_SEQUENCE_DIFFERENCE" in query):
        return (query, renamed, atb_directory, atb_move_directory)
    
    if ("UUFA_ATB_SEQUENCE_DIFFEREN" in query):
        return (query, renamed, atb_directory, atb_move_directory)

    return "Empty" #Leave as last line