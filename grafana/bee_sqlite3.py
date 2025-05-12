import sqlite3

from decouple import Config, RepositoryEnv

env_path = '/opt/bee/beeflow/beesoft/.env'
config = Config(RepositoryEnv(env_path))

conn = sqlite3.connect("/var/lib/grafana/grafana.db")
cursor = conn.cursor()

token_novo = config('TOKEN_API')

cursor.execute("""
    UPDATE dashboard
    SET data = REPLACE(data, 'token-api-beeflow-uuid', ?)
""", (token_novo,))

conn.commit()
conn.close()