import json

if __name__ == "__main__":
    #open json file
    path = '/home/jyh2131/frisky-frog/data/collaboration/covid/bumbeishvili-coronavirus.davidb.dev.json'

    with open(path, 'r') as json_file:
        data = json.load(json_file)
        
        #sort comments by date into date dictionary
        comments_by_date = {}

        for key, subdict in data.items():
            date = subdict['date']
            if date in comments_by_date.keys():
                comments_by_date[date].append(key)
            else:
                comments_by_date[date] = [key]

        print(comments_by_date)

