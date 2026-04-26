CREATE TABLE tournaments (
    id              SERIAL PRIMARY KEY,
    name            VARCHAR(100) NOT NULL,
    status          VARCHAR(20) NOT NULL DEFAULT 'READY',
    created_at      TIMESTAMP NOT NULL DEFAULT NOW()

    -- CONSTRAINT chk_tournament_status
    --     CHECK (status IN ('READY', 'IN_PROGRESS', 'FINISHED'))
);

CREATE TABLE players (
    id              SERIAL PRIMARY KEY,
    tournament_id   INT NOT NULL,
    name            VARCHAR(50) NOT NULL,
    birth           INT NOT NULL

    -- CONSTRAINT fk_players_tournament
    --     FOREIGN KEY (tournament_id)
    --     REFERENCES tournaments(id)
    --     ON DELETE CASCADE
);

CREATE TABLE matches (
    id                  SERIAL PRIMARY KEY,
    tournament_id       INT NOT NULL,
    match_order         INT NOT NULL,

    team_a_player1_id    INT NOT NULL,
    team_a_player2_id    INT NOT NULL,
    team_b_player1_id    INT NOT NULL,
    team_b_player2_id    INT NOT NULL,

    score_a              INT,
    score_b              INT,
    is_tiebreak         BOOLEAN DEFAULT FALSE,

    winner_team         CHAR(1)

    -- CONSTRAINT fk_match_tournament
    --     FOREIGN KEY (tournament_id)
    --     REFERENCES tournaments(id)
    --     ON DELETE CASCADE,

    -- CONSTRAINT fk_teamA_p1 FOREIGN KEY (teamA_player1_id) REFERENCES players(id),
    -- CONSTRAINT fk_teamA_p2 FOREIGN KEY (teamA_player2_id) REFERENCES players(id),
    -- CONSTRAINT fk_teamB_p1 FOREIGN KEY (teamB_player1_id) REFERENCES players(id),
    -- CONSTRAINT fk_teamB_p2 FOREIGN KEY (teamB_player2_id) REFERENCES players(id),

    -- CONSTRAINT chk_no_duplicate_player
    --     CHECK (
    --         teamA_player1_id <> teamA_player2_id AND
    --         teamA_player1_id <> teamB_player1_id AND
    --         teamA_player1_id <> teamB_player2_id AND
    --         teamA_player2_id <> teamB_player1_id AND
    --         teamA_player2_id <> teamB_player2_id AND
    --         teamB_player1_id <> teamB_player2_id
    --     ),

    -- CONSTRAINT chk_winner_team
    --     CHECK (winner_team IN ('A', 'B') OR winner_team IS NULL)
);