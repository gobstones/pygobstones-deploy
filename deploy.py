#!/usr/bin/python

from datetime import datetime
import os, sys
from twisted.trial._dist import options

REPO_DIR = "/home/arypbatista/dev/workspaces/gobstones"


DEPLOY_DIR = REPO_DIR + "/deploy"

BIN_DIR = DEPLOY_DIR + "/bin"
DEB_DIR = DEPLOY_DIR + "/deb"
DEB_TMP_DIR = DEB_DIR + "/dist_tmp"
ZIP_DIR = DEPLOY_DIR + "/zip"
SRC_DIR = DEPLOY_DIR + "/sources"

PYGBS_DIR = SRC_DIR + "/pygobstones"
PYGBSLANG_DIR = SRC_DIR + "/pygobstones-lang"

PYGBS_REPO_URL = "https://github.com/gobstones/pygobstones.git"
PYGBSLANG_REPO_URL = "https://github.com/gobstones/pygobstones-lang.git"

VERSION_FILE = DEPLOY_DIR + "/version"
CHANGELOG_FILE = DEPLOY_DIR + "/changelog.md"

version = []
def package_name(version, branch_name):
    if branch_name == 'master':
        branch_info = ""
    else:
        branch_info = "-%s" % (branch_name,)
    return "pygobstones-%s%s" % (".".join(version), branch_info)


class SystemException(Exception):
    def __init__(self, cmd, error):
        self.cmd = cmd
        self.error = error
        
    def __str__(self):
        return "Error %s got when executed '%s'" % (self.error, self.cmd)

def version_num():
    return ".".join(version)

def sh(cmd):
    result = os.system(cmd)
    if result > 0:
        raise SystemException(cmd, result)
    
def cd(dirname):
    os.chdir(dirname)   


class CodeRepository(object):

    def __init__(self, name, url, directory, deploy_files=[]):
        self.directory = directory
        self.name = name
        self.url = url
        self.deploy_files = deploy_files
        self.pull_additional = lambda:None

    def deploy_to(self, directory):
        for f in self.deploy_files:
            sh("cp -R %s %s" % (self.directory + "/" + f, directory))
            print("cp -R %s %s" % (self.directory + "/" + f, directory))

    def switch_branch(self, branch_name):
        cd(self.directory)

    def clone(self):
        pass
            
    def pull(self):
        if not os.path.exists(self.directory):
            self.clone()
        cd(self.directory)

    def set_pull_additional(self, f):
        self.pull_additional = f
        return self

 
class GitRepository(CodeRepository):

    def pull(self):
        super(GitRepository, self).pull()
        sh("git pull")
        self.pull_additional()
        
    def switch_additional(self, branch):
        pass

    def switch_branch(self, branch):
        super(GitRepository, self).switch_branch(branch)
        sh("git checkout %s" % (branch,))
        self.switch_additional(branch)
        
    def clone(self):
        sh("git clone %s %s" % (self.url, self.directory))

class HgRepository(CodeRepository):

    def pull(self):
        super(HgRepository, self).pull()
        sh("hg pull; hg update")
        
    def clone(self):
        sh("hg clone %s %s" % (self.url, self.directory))

PyGobstonesLangRepo = GitRepository("PyGobstones-Lang",
                                PYGBSLANG_REPO_URL,
                                PYGBSLANG_DIR,
                                ["pygobstoneslang"])

PyGobstonesRepo = GitRepository("PyGobstones", 
                                PYGBS_REPO_URL,
                                PYGBS_DIR, 
                                ["pygobstones", 
                                 "examples", 
                                 "pygobstoneslang",
                                 "pygobstones.py", 
                                 "LICENSE",
                                 "README.md",
                                 "docs",
                                 "AUTHORS",
                                ]).set_pull_additional(lambda:sh('cp %s/pygobstoneslang %s/ -R' % (PYGBSLANG_DIR, PYGBS_DIR)))
                                
# Order matters
REPOSITORIES = [
    PyGobstonesLangRepo, 
    PyGobstonesRepo
]


def log_info(s):
    print("[INFO] " + s)

def checkout_branch(branch_name):
    for r in REPOSITORIES:
        log_info("Checkout %s branch for %s repository" % (branch_name, r.name,))
        r.switch_branch(branch_name)
    cd(DEPLOY_DIR)

def pull_changes():
    for r in REPOSITORIES:
        log_info("Pulling %s repository" % (r.name,))
        r.pull()
    cd(DEPLOY_DIR)

def version_dir(branch_name):
    if branch_name == 'master':
        branch_info = ""
    else:
        branch_info = "-%s" % (branch_name,)
    return BIN_DIR + "/v" + version_num() + branch_info

def deploy(version, branch_name):    
    if os.path.exists(version_dir(branch_name)):
        sh("rm %s -rf" % (version_dir(branch_name),))
    sh("mkdir " + version_dir(branch_name))
    PyGobstonesRepo.deploy_to(version_dir(branch_name))
    #GobstonesRepo.deploy_to(version_dir(branch_name) + "/interpreter/vgbs")
    #XGobstonesRepo.deploy_to(version_dir(branch_name) + "/interpreter/vxgbs")
    cd(DEPLOY_DIR)
    sh("cp %s %s/changelog.txt" % (CHANGELOG_FILE, version_dir(branch_name),))
    sh("echo %s > %s/pygobstones/version" % (".".join(version), version_dir(branch_name)))    
    
def pack_deploy(version, branch_name):
    cd(version_dir(branch_name))
    sh("zip -r %s.zip ./" % (ZIP_DIR + "/" + package_name(version, branch_name),))
    sh("tar -zcvf %s.tar.gz ./" % (ZIP_DIR + "/" + package_name(version, branch_name),))    

def readlines(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    return lines

def readfile(filename):
    return "".join(readlines(filename))

def newfile(filename, s):
    f = open(filename, "w")
    f.write(s)
    f.close()

def load_version():
    version.extend(readlines(VERSION_FILE)[0].strip("\n").split("."))

def save_version(version):
    newfile(VERSION_FILE, ".".join(version))

def changelog_header(version, branch):
    header = "# %s - v%s" % (datetime.now().strftime("%Y-%m-%d"), ".".join(version))
    if branch != 'master':
         header += " (%s)" % (branch,)
    return header

def add_version_to_changelog(filename, version, branch):
    header = changelog_header(version, branch)
    text = header + "\n\n...Version changes here...\n\n\n\n" + readfile(filename)
    newfile(filename, text)

def ask_changelog_info(version, branch):
    add_version_to_changelog(CHANGELOG_FILE, version, branch)
    os.system("vim " + CHANGELOG_FILE)

def push_deployment_script(version):
    cd(DEPLOY_DIR)    
    sh("hg commit -m 'New version %s' -u arypbatista" % (".".join(version),))
    sh("hg push")

def increase_version(version, options):
    part = 1
    if options['mayor']:
        part = 0
    elif options['fix']:
        part = 2
    reset_list = range(part, 2)
    for p in reset_list:
        set_version_part(p+1, 0)
    increase_version_part(part)

def get_version_part(part):
    return int(version[part])
    
def set_version_part(part, value):
    version[part] = str(value)

def increase_version_part(part):        
    set_version_part(part, get_version_part(part)+1)

def build_deb(version, branch_name):
    if os.path.isdir(DEB_TMP_DIR):
        sh("rm %s -rf" % (DEB_TMP_DIR,))
    sh("mkdir %s" % (DEB_TMP_DIR,))
    sh("cp %s %s -R" % (version_dir(branch_name), DEB_TMP_DIR + "/" + package_name(version, branch_name),))    
    cd(DEB_TMP_DIR)    
    sh("cp ../setup.py ./%s" % (package_name(version, branch_name),))
    sh("cp ../pygobstones.desktop ./%s" % (package_name(version, branch_name),))
    sh("tar -zcf %s.tar.gz %s" % (package_name(version, branch_name), package_name(version, branch_name)) )
    sh("py2dsc -m 'Ary Pablo Batista <arypbatista@gmail.com>' %s.tar.gz" % (package_name(version, branch_name),))
    log_info("Copying deb_dist_files.")    
    sh("cp ../deb_dist_files/* deb_dist/%s/debian/" % (package_name(version, branch_name),))    
    cd("deb_dist/%s/" % (package_name(version, branch_name),))
    log_info("Finally building deb.")    
    sh("debuild")    
    cd(DEB_DIR)
    sh("cp %s/deb_dist/%s-1_all.deb %s/versions/" % (DEB_TMP_DIR, package_name(version, branch_name).replace("-","_"), DEB_DIR))


def initialize():
    for r in REPOSITORIES:
        r.clone()

def change_version(version, options):
    if options['minor'] or options['mayor'] or options['fix']:
        increase_version(version, options)

def main(args, options):
    if False and len(args) == 0: #TODO:
        usage()
    elif options['initialize']:
        log_info("Initializing deployment script...")
        initialize()
    elif options['only-pull']:
        log_info("Pulling changes...")
        pull_changes()
    else:
        load_version()
        if options['build-deb']:
            log_info("Building 'deb' package")
            build_deb(version)
        else:
            change_version(version, options)
            checkout_branch(options['branch'])            
            if options['pull']:
                log_info("Pulling changes...")
                pull_changes()
            log_info("Asking for changelog update")
            if options['changelog']:
                ask_changelog_info(version, options['branch'])
            log_info("Deploying new version (v%s)" % (".".join(version),))
            deploy(version, options['branch'])    
            pack_deploy(version, options['branch'])
            log_info("Pushing deployment script.")
            save_version(version)
            push_deployment_script(version)
            log_info("Deployment complete.")        


"""
    Argument parsing
""" 
def default_options(option_switches, defaults):
    opt = {}
    for o in option_switches:
        o = o.split(' ')
        sw = o[0][2:]
        if sw[:3] == 'no-':
            neg = True
            sw = sw[3:]
        else:
            neg = False
        if len(o) == 1:
            opt[sw] = neg
        elif sw in defaults.keys():
            opt[sw] = defaults[sw]
        else:
            opt[sw] = []
    return opt   

def parse_options(option_switches, default_opts, args, max_args=None):
    arguments = []
    opt = default_options(option_switches, default_opts)
    i = 1
    n = len(args)
    while i < len(args):
        o = None
        for oi in option_switches:
            oi = oi.split(' ')
            if oi[0] == args[i]:
                o = oi
                break
        if o is None:
            if len(arguments) == max_args:
                return False
            arguments.append(args[i])
            i += 1
            continue

        sw = o[0][2:]
        if len(o) == 1:
            if sw[:3] == 'no-':
                neg = True
                sw = sw[3:]
            else:
                neg = False
            opt[sw] = not neg
            i += 1
        if len(o) == 2:
            i += 1
            opt[sw] = args[i] 
        else:
            k = 1
            i += 1
            while k < len(o):
                if i >= n: return False
                opt[sw].append(args[i])
                i += 1
                k += 1
    return arguments, opt


SWITCHES = [
    '--initialize',
    '--no-changelog',
    '--mayor',
    '--minor',
    '--fix',
    '--only-pull',
    '--no-pull',
    '--build-deb',
    '--branch X'
]

DEFAULTS = {
    'branch' : 'master'
}

def usage():
    print("Argument needed:")
    print( "\t" + "\n\t".join(SWITCHES))

main(*parse_options(SWITCHES, DEFAULTS, sys.argv))
