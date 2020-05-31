import json

if __name__ == "__main__":
    #open json file
    path = '/home/jyh2131/frisky-frog/data/collaboration/covid/bumbeishvili-coronavirus.davidb.dev.json'
    
    with open(path, 'r') as json_file:
        data = json.load(json_file)
        
        #sort comments by date into date dictionary

        #get adjacency list and list of authors
        adjacency_list = {}
        authors = []
        for majorkey, subdict in data.items():
            comment_author = subdict['comment_author']
            issue_author = subdict['issue_author']

            #append to authors list
            if comment_author not in authors:
                authors.append(comment_author)
            if issue_author not in authors:
                authors.append(issue_author)

            #append to adjacency list
            if comment_author in adjacency_list.keys():
                if issue_author in adjacency_list[comment_author].keys():
                    adjacency_list[comment_author][issue_author] += 1
                else:
                    adjacency_list[comment_author][issue_author] = 1
            else:
                adjacency_list[comment_author] = {issue_author:1}

            #append again to adjacency matrix with issue_author first
            if issue_author in adjacency_list.keys():
                if comment_author in adjacency_list[issue_author].keys():
                    adjacency_list[issue_author][comment_author] += 1
                else:
                    adjacency_list[issue_author][comment_author] = 1
            else:
                adjacency_list[issue_author] = {comment_author:1}
        
        print(adjacency_list)
        #fill in adjacency matrix with 0's
        for i in authors:
            for j in authors:
                if j not in adjacency_list[i].keys():
                    adjacency_list[i][j] = 0

        #create adjacency_matrix
        adjacency_matrix = [[adjacency_list[authors[i]][authors[j]] for i in range(len(authors))] for j in range(len(authors))]
        
        i=0
        for rows in adjacency_matrix:
            print('{:14s}'.format(authors[i]), end =" ")
            i+=1
            print(" ".join(map(str, rows)))