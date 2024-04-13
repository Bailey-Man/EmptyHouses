# scrape the page and query the tables at the following url: https://www.house.gov/representatives
from bs4 import BeautifulSoup
import requests
import html5lib


house_URL = "https://www.house.gov/representatives"

# get senators also ?? how to represent? additional columns

headers = {

}

r = requests.get(url=house_URL)

soup = BeautifulSoup(r.content, 'html5lib')

# loop through all tables found, not just the first one
# mydiv = soup.find_all("div", {"class": "view-content"})

# mytable = soup.find("table", {"class": "table"})

test_tables = soup.find_all("table", {"class": "table"})


house_of_reps_rows = []


for table in test_tables:

    state = table.find("caption").get_text().strip()
    
    new_rows = []
    counter = 0

    # loop thru reps in the state
    for rep in table.find_all("tr"):
        if counter == 0:
            pass 
        # else
        rep_data = rep.contents
        if len(rep_data) > 0:
            for i in rep_data:
                print(i.strip())
        else:
            print(rep_data)

        # print(rep_data)

        # # todo: skip first rep in each table
        # new_info = {}
        # new_info['District'] = rep
        # new_info['Name'] = 



        if counter == 2:
            break
        else: 
            counter += 1
        # new_info['district'] = rep
        new_rows.append(new_info)



    break



    # print(len(reps))


    print(state)



# print(len(mytable), len(test_tables))

# for state in mytables


# rows = []
# for row in mytables.find_all("tr"):
#     cells = row.find_all("td")
#     row_data = [cell.text.strip() for cell in cells]
#     rows.append(row_data)

# print(len(rows))
# print(soup.prettify())
