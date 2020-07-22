from fastapi import APIRouter, Depends

from app.core.repository import get_repository
from app.domain.stock_example.models import Stock
from app.domain.user.models import User

router = APIRouter()
repository =get_repository()


@router.get("/")
async def home():
    return {"conexao back e front": "funcionando"}

@router.post("/form")
async def post(
        repository = Depends(get_repository)):
    user1 = User(id='12345',name='guto5',supervisor ='supervisor5',status='status5')
    stock1 = Stock(id=1,symbol='ahhaha')
    repository.save(user1)
    repository.save(stock1)
    return {"usuario": "criado"}




