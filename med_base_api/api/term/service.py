import uuid as uuid_pkg

import ops as ops
from api.term import schemas
from api.term.models import Term
from service import Service
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class TermService(Service):
    async def get_objects(
        self,
        session: AsyncSession,
    ) -> list[schemas.TermWithId]:
        """
        Логика http-метода get для извлечения всех медицинских терминов.

        Args:
            session (AsyncSession): Асинхронная Sqlalchemy сессия.

        Returns:
            list[schemas.TermWithId]: Список медицинских терминов.
        """
        statement = select(Term)
        terms: list[Term] = await ops.execute_to_get_many(statement, session)

        return [schemas.TermWithId.model_validate(term) for term in terms]

    async def get_object(
        self,
        term_id: uuid_pkg.UUID,
        session: AsyncSession,
    ) -> schemas.TermWithId:
        """
        Логика http-метода get для извлечения одного медицинского термина.

        Args:
            term_id (uuid_pkg.UUID): id медицинского термина.
            session (AsyncSession): Асинхронная Sqlalchemy сессия.

        Raises:
            EntityNotFoundException: Медицинский термин не найдена.

        Returns:
            schemas.TermWithId: Медицинский термин.
        """
        term = await ops.get_one_by_id(Term, term_id, session)
        return schemas.TermWithId.model_validate(term)

    async def create_object(
        self,
        term: schemas.TermBase,
        session: AsyncSession,
    ) -> schemas.TermWithId:
        """
        Логика http-метода post для создания медицинского термина.

        Args:
            term (schemas.TermBase): Pydantic схема медицинского термина.
            session (AsyncSession): Асинхронная Sqlalchemy сессия.

        Raises:
            DBIntegrityException: Вставка нарушает целостность бд.

        Returns:
            schemas.TermWithId: Медицинский термин.
        """

        term_sqlalchemy_object = await ops.create(
            Term,
            term.model_dump(),
            session,
        )
        return schemas.TermWithId.model_validate(term_sqlalchemy_object)

    async def update_object(
        self,
        term_id: uuid_pkg.UUID,
        term: schemas.TermBase,
        session: AsyncSession,
    ) -> schemas.TermWithId:
        """
        Логика http-метода put для обновления медицинского термина.

        Args:
            term_id (uuid_pkg.UUID): id медицинского термина.
            term (schemas.TermBase): Pydantic схема медицинского термина.
            session (AsyncSession): Асинхронная Sqlalchemy сессия.

        Raises:
            DBIntegrityException: Обновление нарушает целостность бд.

        Returns:
            schemas.TermWithId: Медицинский термин.
        """
        term_sqlalchemy_object = await ops.update(
            Term,
            term_id,
            term.model_dump(),
            session,
        )
        return schemas.TermWithId.model_validate(term_sqlalchemy_object)

    async def delete_object(
        self,
        term_id: uuid_pkg.UUID,
        session: AsyncSession,
    ) -> schemas.TermWithId:
        """
        Логика http-метода delete для удаления медицинского термина.

        Args:
            term_id (uuid_pkg.UUID): id медицинского термина.
            session (AsyncSession): Асинхронная Sqlalchemy сессия.

        Raises:
            DBIntegrityException: Удаление нарушает целостность бд.

        Returns:
            schemas.TermWithId: Медицинский термин.
        """

        term = await ops.delete(Term, term_id, session)
        return schemas.TermWithId.model_validate(term)


term_service = TermService()