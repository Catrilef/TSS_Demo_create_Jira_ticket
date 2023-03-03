import os
from jira import JIRA

# Jira connextion
jira_conn = JIRA(options={'server': os.environ['TSS_JIRA_SERVER']}, 
                 basic_auth=(os.environ['TSS_JIRA_USER'], os.environ['TSS_JIRA_PASS']))


#______________________________________________________________
# Para hacer pruebas libres usar este template
issue_dict_test = {
    'project': 'TESTING',  #debe ser la clave del proyecto
    'summary': 'Quotation error test',
    'description': 'Prueba de creacion de tickets',
    'issuetype': 'Incidente',
    'customfield_10672':  {'value': "BOT"} #2#'BODEGA TULTITLÁN'
}

#_______________________________________________________________
# Para crear ticket de quotation error usar este template
# USAR 1 tickt por cada QTN para facilitar el análisis
QTN = 'asd123asd' # qtn a alertar
issue_dict = {
    'project': 'MST',  #No cambiar!
    'summary': 'Quotations Error',
    'description': 'Error en bla bla bla... %s' % QTN,
    'issuetype': 'QTN Error', #No cambiar!
    'customfield_10673':  {'value': "BOT"}, # No cambiar!
}
#_____________________________________________________________


issue_key = jira_conn.create_issue(fields=issue_dict_test) 
#issue_key = jira_conn.create_issue(fields=issue_dict) 
print ('The Ticket has been created as',issue_key)
