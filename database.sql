CREATE DATABASE IF NOT EXISTS careercraft;
USE careercraft;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS user_profiles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    phone VARCHAR(15),
    address TEXT,
    education TEXT,
    skills TEXT,
    projects TEXT,
    awards TEXT,
    experience TEXT,
    linkedin_url VARCHAR(255),
    github_url VARCHAR(255),
    portfolio_url VARCHAR(255),
    font_size VARCHAR(10) DEFAULT '14px',
    font_family VARCHAR(50) DEFAULT 'Inter',
    template_id INT DEFAULT 1,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
