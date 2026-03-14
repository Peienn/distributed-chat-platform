async function initDB(pool) {

  await pool.query(`
    CREATE TABLE IF NOT EXISTS users (
      id SERIAL PRIMARY KEY,
      username VARCHAR(50) NOT NULL UNIQUE,
      created_at TIMESTAMP DEFAULT now(),
      last_login_at TIMESTAMP
    );
  `);

  await pool.query(`
    CREATE TABLE IF NOT EXISTS messages (
      id SERIAL PRIMARY KEY,
      user_id INTEGER,
      username VARCHAR(50) NOT NULL,
      text TEXT NOT NULL,
      created_at TIMESTAMP DEFAULT now(),
      CONSTRAINT messages_user_id_fkey
        FOREIGN KEY (user_id)
        REFERENCES users(id)
    );
  `);

  await pool.query(`
    CREATE INDEX IF NOT EXISTS idx_messages_created_at
    ON messages(created_at);
  `);

  await pool.query(`
    CREATE INDEX IF NOT EXISTS idx_messages_user_created
    ON messages(user_id, created_at);
  `);

  await pool.query(`
    CREATE INDEX IF NOT EXISTS idx_messages_username
    ON messages(username);
  `);

  await pool.query(`
    CREATE TABLE IF NOT EXISTS analysis_results (
      id SERIAL PRIMARY KEY,
      batch_id VARCHAR(64) NOT NULL,
      room_id VARCHAR(64),
      messages JSONB NOT NULL,
      analysis TEXT NOT NULL,
      created_at TIMESTAMP DEFAULT now()
    );
  `);

  await pool.query(`
    CREATE INDEX IF NOT EXISTS idx_analysis_batch_id
    ON analysis_results(batch_id);
  `);

  console.log("Database initialized");
}

module.exports = initDB;