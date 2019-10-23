import webbrowser

###### URL LIST #######

# Learning_materials github repository
urls = ['https://github.com/rpclancy/learning_materials']
# Other atmospheric science github repositories
urls.append("https://github.com/topics/atmospheric-science")
# Explains how webbroswer module works
urls.append("https://pythonforbeginners.com/code-snippets-source-code/python-webbrowser")
# Explains how to use python in visualstudio
urls.append("https://code.visualstudio.com/docs/python/python-tutorial")
# Good intro to Git
urls.append('https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud')
urls.append('https://www.atlassian.com/git/tutorials/comparing-workflows')
# For when you get in trouble with git
urls.append('https://ohshitgit.com/')

###### Open URLS #######
for url in urls: 
    webbrowser.open(url, new=1)

print('Done')