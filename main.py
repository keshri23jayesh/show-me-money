# main.py
import logging

from fastapi import FastAPI, HTTPException

from services.response import BalanceSheetResponse
from services.xero_service import XeroService
from config import settings

app = FastAPI()

xero_service = XeroService(base_url=settings.xero_api_base_url)


@app.get("/api/balance-sheet", response_model=BalanceSheetResponse)
async def get_balance_sheet():
    try:
        return xero_service.get_balance_sheet()
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
