# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Django e-commerce marketplace for local food producers in Bristol, UK. Users have one of three roles: customer, producer, or admin. The project is organized into four vertical-slice apps, each owned by a different team member.

## Commands

```bash
# Local development (SQLite)
python manage.py runserver

# Docker development (PostgreSQL — matches production)
docker compose up
docker compose exec web python manage.py seed_data   # Populate demo data

# Database
python manage.py makemigrations <app_name>
python manage.py migrate

# Tests
python manage.py test                    # All tests
python manage.py test accounts           # Single app
python manage.py test accounts.tests.TestClassName  # Single class
```

## Architecture

### App Ownership (Vertical Slices)
- **accounts** — Custom user model, registration, profiles, role-based decorators
- **products** — Product catalog, inventory, seasonal/allergen data, search
- **cart** — Shopping cart, checkout, order history
- **orders** — Order processing, status workflows, payment settlements

### Auth & Access Control
`accounts.User` extends `AbstractUser` with email-only login (no username field). Role enforcement is done via decorators:
```python
@producer_required
@customer_required
@role_required('admin')
```
These are defined in `accounts/` and imported by other apps.

### Key Business Rules
- **Commission:** 5% network fee applied at checkout; recorded on `Payment` model
- **Delivery:** 48-hour minimum lead time enforced at checkout
- **Order numbers:** Auto-generated as `BFN-{UUID}`
- **Payment IDs:** Mock sandbox transactions as `SBX-{UUID}`
- **Stock:** Decremented on order placement; `CartItem` requires stock check before checkout
- **Order state machine:** `pending → confirmed → ready → delivered` — transitions validated server-side, producers drive status updates

### Data Model Notes
- `Cart` groups `CartItem`s; items are grouped by producer in templates
- `OrderItem` snapshots price at order time (price is immutable post-order)
- `Product` allergens stored as a JSON array field
- `CustomerProfile` and `ProducerProfile` are `OneToOne` extensions of the User model
- Cart item count is injected globally via `cart.context_processors.cart_count` (registered in settings)

### Database
- Local: SQLite (auto-selected when `DATABASE_HOST` env var is absent)
- Docker: PostgreSQL 15 (auto-selected when `DATABASE_HOST` is set)

### Templates
Inheritance via `templates/base.html`. Navbar is role-aware. Bootstrap 5 loaded from CDN.

## Key Files
- `config/settings.py` — Django settings, app list, session timeout (1 hour), timezone (Europe/London)
- `config/urls.py` — Root URL conf; includes each app's `urls.py`
- `BFN_Sprint2_Project_Prompt.md` — Full project spec, test case matrix (17 Sprint 2 + 8 Sprint 3 tests), seed data spec
