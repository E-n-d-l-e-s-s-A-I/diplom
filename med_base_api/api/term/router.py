import uuid as uuid_pkg
from typing import Annotated

from api.term import schemas
from api.term.service import term_service
from database import get_db_session
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/term", tags=["Медицинские термины"])


@router.get("")
async def get_terms(
    session: Annotated[AsyncSession, Depends(get_db_session)],
) -> list[schemas.TermWithId]:
    """
    Эндпойнт для получения всех медицинских терминов.

    Returns:
        list[schemas.TermWithId]: Список медицинских терминов.
    """
    result: list[schemas.TermWithId] = await term_service.get_objects(session)
    return result


@router.get("/{term_id}")
async def get_term(
    session: Annotated[AsyncSession, Depends(get_db_session)],
    term_id: uuid_pkg.UUID,
) -> schemas.TermWithId:
    """
    Эндпойнт для получения конкретного медицинского термина.

    Args:
        term_id (uuid_pkg.UUID): Идентификатор медицинского термина.

    Returns:
        schemas.TermWithId: Медицинский термин.
    """
    return await term_service.get_object(term_id, session)


@router.post("")
async def create_term(
    session: Annotated[AsyncSession, Depends(get_db_session)],
    term: schemas.TermBase,
) -> schemas.TermWithId:
    """
    Эндпойнт для создания медицинского термина.

    Args:
        term (schemas.TermBase): Медицинский термин.
    Returns:
        schemas.TermWithId: Медицинский термин.
    """
    return await term_service.create_object(
        term,
        session,
    )


@router.put("/{term_id}")
async def update_term(
    session: Annotated[AsyncSession, Depends(get_db_session)],
    term_id: uuid_pkg.UUID,
    term: schemas.TermBase,
) -> schemas.TermWithId:
    """
    Эндпойнт для обновления медицинского термина.

    Args:
        term_id (uuid_pkg.UUID): Идентификатор медицинского термина.
        term (schemas.TermBase): Медицинский термин.

    Returns:
        schemas.TermWithId: Медицинский термин.
    """
    return await term_service.update_object(
        term_id,
        term,
        session,
    )


@router.delete("/{term_id}")
async def delete_term(
    session: Annotated[AsyncSession, Depends(get_db_session)], term_id: uuid_pkg.UUID
) -> schemas.TermWithId:
    """
    Эндпойнт для удаления медицинского термина.

    Args:
        term_id (uuid_pkg.UUID): Идентификатор медицинского термина.

    Returns:
        schemas.TermWithId: Медицинский термин.
    """
    return await term_service.delete_object(term_id, session)