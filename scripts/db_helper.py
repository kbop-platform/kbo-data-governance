#!/usr/bin/env python3
"""scripts/db_helper.py - MSSQL 공통 연결 모듈

프로젝트 .env 기반으로 pymssql 연결을 생성하는 단일 진입점.
"""
import os
import pymssql
from config import load_env


def get_connection(database="master", *, timeout=30, login_timeout=15):
    """프로젝트 .env 기반 MSSQL 연결 반환.

    Args:
        database: 연결할 DB명 (기본 master)
        timeout: 쿼리 타임아웃 (초)
        login_timeout: 로그인 타임아웃 (초)

    Returns:
        pymssql.Connection
    """
    load_env()
    return pymssql.connect(
        server=os.environ.get("MSSQL_SERVER", ""),
        port=int(os.environ.get("MSSQL_PORT", "1433")),
        user=os.environ.get("MSSQL_USER", ""),
        password=os.environ.get("MSSQL_PASSWORD", ""),
        database=database,
        login_timeout=login_timeout,
        timeout=timeout,
        charset="UTF-8",
    )
