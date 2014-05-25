from core import send_request, get_auth
from people import get_me
from projects import get_all_active_projects, get_project
from todo_lists import get_todo_list, get_todo, get_all_active_todo_lists
from stars import get_starred_projects
try:
    from MY_BC import BC
except ImportError:
    from core import MY_BC_NUMBER as BC

class Camper(object):
    def __init__(self,**kwargs):
        if kwargs.get('name',False):
            self.name = kwargs['name']
        if kwargs.get('id',False):
            self.id = kwargs['id']
        if kwargs.get('email_address',False):
            self.email_address = kwargs['email_address']
        if kwargs.get('admin',False):
            self.admin = kwargs['admin']
        if kwargs.get('created_at',False):
            self.created_at = kwargs['created_at']
        if kwargs.get('updated_at',False):
            self.updated_at = kwargs['updated_at']
        if kwargs.get('starred_projects',False):
            self._starred_projects = kwargs['starred_projects']
        if kwargs.get('active_projects',False):
            self._active_projects = kwargs['active_projects']
        if kwargs.get('events',False):
            self._events = kwargs['events']
        if kwargs.get('assigned_todos',False):
            self._assigned_todos = kwargs['assigned_todos']
        if kwargs.get('avatar_url',False):
            self.avatar_url = kwargs['avatar_url']
        if kwargs.get('fullsize_avatar_url',False):
            self.fullsize_avatar_url = kwargs['fullsize_avatar_url']
        self.todos = send_request(url=self._assigned_todos['url'])
        self.assigned_todos = []
        for bucket in self.todos:
            self.assigned_todos.append(bucket['assigned_todos'])
        #self.starred_projects = send_request(url=self._starred_projects['url'])
        self.events = send_request(url=self._events['url'])
        #self.active_projects = send_request(url=self._active_projects['url'])


    def get_avatar(self,filename):
        fp = open(filename,'wb')
        data = send_request(url=self.avatar_url,json=False)
        fp.write(data.content)
        fp.close()


class BaseCampPerson(object):
    BC_ACCOUNT_NUM = BC
    

class BaseCamper(BaseCampPerson):
    def __init__(self):
        self._internal_camper = Camper(**get_me())
        self._todos = []
        for attr in dir(self._internal_camper):
            if not attr.startswith('_'):
                setattr(self,attr,getattr(self._internal_camper,attr))
        self._get_todos()
        self._get_projects()

    def __getitem__(self,key):
        if key in dir(self._internal_camper):
            return self._internal_camper.__dict__[key]

    def _get_todos(self):
        self._todo_buckets = []
        for bucket in self.assigned_todos:
            tmp = []
            for todo in bucket:
                res = send_request(url=todo['url'])
                tmp.append(res)
                self._todos.append(res)
            self._todo_buckets.append(tmp)

    def _get_projects(self):
        self.pm = BCProjectManager(self)

    @staticmethod
    def send_basecamp_request(url):
        return send_request(url=url,auth=get_auth())

    @property 
    def todo_buckets(self):
        return self._todo_buckets

    @property
    def current_todos(self):
        return self._todos

    @property
    def todo_count(self):
        return len(self._todos)

    @property
    def event_count(self):
        return len(self.events)


class BCProjectManager(object):
    def __init__(self,camper):
        self.bc = camper
        self.projects = get_all_active_projects(self.bc.BC_ACCOUNT_NUM)

    def get_project(self,pid):
        return get_project(self.bc.BC_ACCOUNT_NUM,pid)

    def get_projects(self):
        return self.projects

    def get_project_todolists(self,pid):
        for proj in self.projects:
            if proj['id'] == pid:
                return send_request(url=proj['todolists']['url'],auth=get_auth())
        return None
    
