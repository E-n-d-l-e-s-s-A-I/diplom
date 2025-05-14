#!/bin/bash
COMMAND="${1:-payment_service}"

case $COMMAND in
    med_base_api)
        echo "Запускается сервис med_base_api..."
        cd med_base_api
        alembic upgrade head
        python cli.py filldb
        uvicorn main:app --host 0.0.0.0 --port 8000 --reload
        ;;
    admin)
        cd admin
        streamlit run main.py --client.showErrorDetails=false
       ;;
    synomed_api)
        cd synomed_api
        uvicorn main:app --host 0.0.0.0 --port 8000 --reload
       ;;
    *)
        echo "Ошибка: Неверный параметр '$COMMAND'. Используйте 'med_base_api' или 'admin' или 'synomed_api'"
        exit 1
        ;;
esac