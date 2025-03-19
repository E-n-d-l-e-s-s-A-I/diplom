#!/bin/bash
COMMAND="${1:-payment_service}"

case $COMMAND in
    med_base_api)
        echo "Запускается сервис med_base_api..."
        cd med_base_api
        uv run alembic upgrade head
        python cli.py filldb
        uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
        ;;
    admin)
        cd admin
        uv run streamlit run main.py --client.showErrorDetails=false
       ;;
    *)
        echo "Ошибка: Неверный параметр '$COMMAND'. Используйте 'med_base_api' или 'admin' или 'synomed_api'"
        exit 1
        ;;
esac