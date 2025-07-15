from scr.database.db_service import get_analysis_data

def returm_analysis_lmm():
    return provide_analysis(get_analysis_data())

def provide_analysis(data_from_lmm):
    return data_from_lmm