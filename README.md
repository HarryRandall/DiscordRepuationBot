# Discord Rep Bot

A custom bot designed for Discord servers that manage reputation (rep) transactions, ideal for servers offering services like middleman transactions. This bot simplifies the process of awarding and tracking reputation for users, automating much of the workload for server moderators.

---

## What is the Bot?

This bot allows users in a Discord server to give, track, and manage reputation points with ease. The bot is particularly useful for communities where reputation is essential, such as trading or middleman services. With customizable commands, the bot handles transactions, checks user reputation, and provides error handling to streamline interactions.

---

## Features

- **Reputation System:** Users can give reputation points to others with proof, track transaction history, and check their own or others' reputation.
- **Custom Commands:** Includes commands like `+rep`, `+check`, `+add`, and `+remove` with input validation to ensure data integrity.
- **Error Handling:** Provides feedback for incorrect usage, missing permissions, and unrecognized users.
- **Restricted Channels:** Commands are limited to designated channels for better organization and control.

---

## Commands

### +Add
- **Usage:** `+add (@User) (Amount of rep) (Amount of money)`
- **Access:** Moderator-only command to increase a user's reputation and transaction amount.

### +Remove
- **Usage:** `+remove (@User) (Amount of rep) (Amount of money)`
- **Access:** Moderator-only command to reduce a user's reputation and transaction amount.

### +Rep
- **Usage:** `+rep (@user) (Amount of money in the trade) (Screenshot URL: Gyazo or Imgur for proof)`
- **Purpose:** Allows users to give reputation to another user for completed trades, including a required proof link.

### +Help
- **Usage:** `+help`
- **Purpose:** Provides help options, including syntax for each command.

---

## Setup

1. **Install Required Packages:** Ensure you have all dependencies installed as specified in `requirements.txt`.
2. **Edit Prefix & Channel IDs:** Open the code, modify the prefix and channel IDs to match your server setup.
3. **Run the Bot:** Launch the bot to start using it in your server.

---

## Troubleshooting

If you encounter any issues or have questions, please feel free to reach out on Discord at: `Redacted`.

---

## Additional Information

The **Interstellar Lounge Discord Bot** is a customized bot crafted for managing user reputation in Discord servers. With advanced features for error handling and command restriction, it aims to improve server moderation efficiency and user experience.

---
