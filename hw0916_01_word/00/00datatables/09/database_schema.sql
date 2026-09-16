CREATE DATABASE IF NOT EXISTS english3570 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE english3570;
CREATE TABLE vocabulary (
  id INT PRIMARY KEY,
  word VARCHAR(100) NOT NULL UNIQUE,
  category ENUM('core_3000','AWL_570') NOT NULL,
  part_of_speech VARCHAR(40) NULL,
  definition_zh_tw TEXT NULL,
  example_en TEXT NULL,
  example_zh_tw TEXT NULL,
  ipa_us VARCHAR(100) NULL,
  audio_url VARCHAR(500) NULL,
  note TEXT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX idx_word(word),
  INDEX idx_category(category)
);
