from .user import UserCRUD
from .post import PostCRUD

# 필요한 함수들을 여기서 import해서 외부에 노출

# crud.user, crud.post 형식으로 사용하기 위해
user = UserCRUD()
post = PostCRUD()
