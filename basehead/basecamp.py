from core import send_request
from people import get_me
from projects import get_all_active_projects, get_project
from todo_lists import get_todo_list, get_todo, get_all_active_todo_lists
from stars import get_starred_projects
from MY_BC import BC

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
