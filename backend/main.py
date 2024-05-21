# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests

url = "https://pesquisa.in.gov.br/imprensa/core/jornalList.action"

# payload = "__checkbox_edicao.jornal=1%2C1000%2C1010%2C1020%2C515%2C521%2C522%2C531%2C535%2C536%2C523%2C532%2C540%2C1040%2C2%2C2000%2C529%2C525%2C3%2C3000%2C3020%2C1040%2C526%2C530%2C600%2C601%2C602%2C603%2C604%2C605%2C606%2C607%2C608%2C609%2C610%2C611%2C612%2C613%2C614%2C615%2C616%2C617%2C618%2C619%2C620%2C621%2C622%2C623%2C624%2C625%2C626%2C627%2C628%2C629%2C630%2C631%2C632%2C634%2C635%2C636%2C637%2C638%2C639%2C640%2C641%2C642%2C643%2C644%2C645%2C646%2C647%2C648%2C649%2C650%2C651%2C652%2C653%2C654%2C655%2C656%2C657%2C658%2C659%2C660%2C661%2C662%2C663%2C664%2C665%2C666%2C667%2C668%2C669%2C670%2C671%2C701%2C702&__checkbox_edicao.jornal=1%2C1000%2C1010%2C1020%2C515%2C521%2C522%2C531%2C535%2C536%2C523%2C532%2C540%2C1040%2C600%2C601%2C602%2C603%2C612%2C613%2C614%2C615%2C701&__checkbox_edicao.jornal=2%2C2000%2C529%2C525%2C604%2C605%2C606%2C607%2C702&__checkbox_edicao.jornal=3%2C3000%2C3020%2C1040%2C526%2C530%2C608%2C609%2C610%2C611&edicao.jornal_hidden=1%2C1000%2C1010%2C1020%2C515%2C521%2C522%2C531%2C535%2C536%2C523%2C532%2C540%2C1040%2C2%2C2000%2C529%2C525%2C3%2C3000%2C3020%2C1040%2C526%2C530%2C600%2C601%2C602%2C603%2C604%2C605%2C606%2C607%2C608%2C609%2C610%2C611%2C612%2C613%2C614%2C615%2C616%2C617%2C618%2C619%2C620%2C621%2C622%2C623%2C624%2C625%2C626%2C627%2C628%2C629%2C630%2C631%2C632%2C634%2C635%2C636%2C637%2C638%2C639%2C640%2C641%2C642%2C643%2C644%2C645%2C646%2C647%2C648%2C649%2C650%2C651%2C652%2C653%2C654%2C655%2C656%2C657%2C658%2C659%2C660%2C661%2C662%2C663%2C664%2C665%2C666%2C667%2C668%2C669%2C670%2C671%2C701%2C702&edicao.txtPesquisa=&edicao.dtInicio=17%2F05&edicao.dtFim=17%2F05&edicao.ano=2004&edicao.jornal=2%2C2000%2C529%2C525%2C604%2C605%2C606%2C607%2C702&edicao.fonetica=null&jornal=do2&g=68942&t=com.liferay.journal.model.JournalArticle"

payload = {
    '__checkbox_edicao.jornal': [1,1000,1010,1020,515,521,522,531,535,536,523,532,540,1040,2,2000,529,525,3,3000,3020,
                                 1040,526,530,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,
                                 618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,634,635,636,637,638,639,
                                 640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,
                                 661,662,663,664,665,666,667,668,669,670,671,701,702],
    '__checkbox_edicao.jornal': [1,1000,1010,1020,515,521,522,531,535,536,523,532,540,1040,600,601,602,603,612,613,614,
                                 615,701],
    '__checkbox_edicao.jornal': [2,2000,529,525,604,605,606,607,702],
    '__checkbox_edicao.jornal': [3,3000,3020,1040,526,530,608,609,610,611],
    'edicao.jornal_hidden': [1,1000,1010,1020,515,521,522,531,535,536,523,532,540,1040,2,2000,529,525,3,3000,3020,1040,
                             526,530,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,
                             620,621,622,623,624,625,626,627,628,629,630,631,632,634,635,636,637,638,639,640,641,642,
                             643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,
                             665,666,667,668,669,670,671,701,702],
    'edicao.txtPesquisa': '',
    'edicao.dtInicio': '17/05', # mudar aqui e nos três campos abaixo para o dia e ano desejado
    'edicao.dtFim': '17/05',
    'edicao.ano': '2004',
    'edicao.jornal': [2, 2000, 529, 525, 604, 605, 606, 607, 702],
    'edicao.fonetica': None,
    'jornal': 'do2',
    'g': '68942',
    't': 'com.liferay.journal.model.JournalArticle'
}



headers_EXAMPLE = {
    "cookie": "ALTERAR",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://www.in.gov.br",
    "priority": "u=0, i",
    "referer": "https://www.in.gov.br/",
    "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}




from networking import body_request

headers = body_request.headers

if __name__ == '__main__':
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)