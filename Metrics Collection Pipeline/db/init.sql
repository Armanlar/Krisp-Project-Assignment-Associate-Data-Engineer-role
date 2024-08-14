
CREATE TABLE user_metrics (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    session_id INT NOT NULL,
    talked_time INT,
    microphone_used BOOLEAN,
    speaker_used BOOLEAN,
    voice_sentiment TEXT,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    device_type TEXT
);

CREATE INDEX idx_user_id ON user_metrics(user_id);
CREATE INDEX idx_session_id ON user_metrics(session_id);
CREATE INDEX idx_timestamp ON user_metrics(timestamp);