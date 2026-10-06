import json
class UserManager:
    def __init__(self):
        self.users = {}
        self.id = 1
    def add_user(self,name,age):
        new_id = self.id
        self.id += 1
        user={"id":new_id,"name":name,"age":age}
        self.users[new_id]=user
        return user
    def get_user(self,user_id):
        return self.users.get(user_id)
    def update_age(self,user_id,new_age):
            if user_id in self.users:
                self.users[user_id]["age"]=new_age
                return True
            else:
                return False
    def remove_user(self,user_id):
         if user_id in self.users:
              del self.users[user_id]
              return True
         else:
              return False
    def list_users(self):
         return list(self.users.value())
    def save_to_json(self,filepath):
         user_list=self.list_users()
         with open(filepath,'w',encoding='utf-8')as f:
                   json.dump(user_list,f,ensure_ascii=False)
    def load_from_json(self,filepath):
        self.users.clear()
        try:
                with open(filepath,'r',encoding='utf-8')as f:
                   users_list=json.load(f)
                mid=0
                for user in users_list:
                   uid=user["id"]
                   self.users[uid]=user
                   if uid > mid:
                        mid=uid
                self.id=mid+1
        except Exception:
             self.id = 1
