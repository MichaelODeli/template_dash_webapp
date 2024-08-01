create table
  "users" (
    "id" serial primary key,
    "first_name" varchar(50) not null,
    "middle_name" varchar(50),
    "last_name" varchar(50) not null,
    "username" varchar(70) not null,
    "email" varchar(150) not null,
    "password" varchar(64) not null,
    "active" BOOLEAN DEFAULT TRUE,
    "created_at" timestamp not null default NOW(),
    "updated_at" timestamp not null default NOW(),
    FOREIGN KEY (position_id) REFERENCES positions (id) ON DELETE CASCADE,
    UNIQUE(email),
    UNIQUE(username)
  );