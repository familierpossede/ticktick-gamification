# TickTick Gamification Plugin (Read-Only)

This is a ready-to-deploy backend and plugin for your Custom GPT that connects to TickTick to gamify your habit tasks with coins, XP, and streak tracking.

## Features
- OAuth2 authentication with TickTick
- Read-only access to fetch today’s tasks and recurring habit tasks
- Secure FastAPI backend
- OpenAPI and Plugin manifest included

## 1-Click Deploy to Render
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

## Setup
1. Fork this repo to your GitHub account.
2. Click the Deploy button above.
3. In the Render dashboard, set the following environment variables:
   - `TICKTICK_CLIENT_ID`
   - `TICKTICK_CLIENT_SECRET`
   - `TICKTICK_REDIRECT_URI` (e.g., `https://yourapp.onrender.com/api/oauth/callback`)

4. Wait for deployment to finish.
5. Use the hosted URLs to update your `ai-plugin.json` and `openapi.yaml` files and upload to GPT Builder.

That's it — you're live!
