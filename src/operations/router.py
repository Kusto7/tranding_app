import time

from fastapi import APIRouter, Depends
from sqlalchemy import select, inspect, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from operations.models import operation
from operations.schemas import OperationCreate
from fastapi_cache.decorator import cache

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("/long_operations")
@cache(expire=30)
def long_operation():
    time.sleep(2)
    return "Dlinnaya slovestnaya postoviza"


@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == operation_type)
    result = await session.execute(query)
    return result.all()


@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
