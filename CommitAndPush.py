import git
from git import Repo
from git import RemoteProgress

def commit_to_remote_repo(repository_path , moniker_name , branch_name , commit_message , remote_repo = 'origin'):
    '''
    Commit and Push to remote repo.
    
    repository_path: path to working repository which contains the .git directory.
    
    moniker_name: list of modified files.
    
    branch_name: Name of branch under which you want to commit and push.
    
    commit_message: commit message
    
    remote_repo: where you want to push
    
    '''
    try:
        #Gives object which represent our repository  
        repo = Repo(repository_path)
    
        #staging of all the modified files passed in the form of list
        repo.git.add(moniker_name)
    
        #print the current status
        #print(repo.git.status())
    
        #commit all the changes with message
        repo.git.commit(m = commit_message)
    
        #Now all the commited changes are pushed to remote repo
        repo.git.push(remote_repo , branch_name)
    
    except:
        print('Commiting and pushing is unsuccesful.')
        
        
        
        
def clone_repo(url , to_path , branch_name='master' , isProgress='no'):
    '''
    Create a clone from the given URL
    
    url: valid git url
    
    to_path: Path to which the repository should be cloned to
    
    branch_name: which branch of remote repo you want to clone
    
    isProgress: if you want to see the progress(takes 'yes' or 'no' as input)
    
    return: Repo instance pointing to the cloned directory
    '''
    
    if(isProgress == 'yes'):
        class MyProgressPrinter(RemoteProgress):
            def update(self, op_code, cur_count, max_count=None, message=''):
                print(self._cur_line)
        
        print('Cloning into %s' % to_path)
    
        y = git.Repo.clone_from(url,to_path, branch=branch_name, progress=MyProgressPrinter())
    
    else:
        print('Cloning into %s' % to_path)
    
        y = git.Repo.clone_from(url,to_path, branch=branch_name)
        
    return y
        
   

        