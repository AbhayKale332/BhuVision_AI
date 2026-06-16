This structure follows a simple idea:

```text
UI Pages
   ↓
Features
   ↓
Services
   ↓
FastAPI
```

---

# src/

```text
src/
```

All frontend code lives here.

---

# app/

```text
src/app/
```

Next.js App Router.

Every folder here becomes a route.

Example:

```text
app/map/page.tsx
```

becomes

```text
/map
```

---

## (auth)/

```text
app/(auth)/
```

Route group.

Used for:

```text
/login
/register
/forgot-password
```

The `( )` does not appear in URL.

Only for organization.

---

## dashboard/

```text
app/dashboard/
```

Main user dashboard.

Example:

```text
/dashboard
```

---

## map/

```text
app/map/
```

Map viewing page.

This will become one of the biggest parts of your project.

Examples:

```text
/map
/map/project/123
```

---

## models/

```text
app/models/
```

Model marketplace pages.

Examples:

```text
/models
/models/123
```

---

## publishers/

```text
app/publishers/
```

Publisher profile pages.

Examples:

```text
/publishers
/publishers/akash
```

---

# components/

```text
src/components/
```

Reusable UI pieces.

Think LEGO blocks.

---

## ui/

```text
components/ui/
```

Shadcn components.

Examples:

```text
Button
Dialog
Card
Input
```

Usually auto-generated.

---

## map/

```text
components/map/
```

Map-specific components.

Examples:

```text
MapViewer
LayerSwitcher
CoordinatePanel
AOITool
```

---

## layout/

```text
components/layout/
```

Application layout.

Examples:

```text
Navbar
Sidebar
Footer
```

Used on many pages.

---

## shared/

```text
components/shared/
```

Reusable components.

Examples:

```text
Loader
ErrorCard
Pagination
```

Used everywhere.

---

# features/

```text
src/features/
```

Actual business logic.

This is where real frontend development happens.

---

Think:

```text
components = how it looks

features = what it does
```

---

## auth/

```text
features/auth/
```

Authentication logic.

Examples:

```text
login
logout
register
token refresh
```

---

## users/

```text
features/users/
```

User-related functionality.

Examples:

```text
profile update
avatar upload
settings
```

---

## maps/

```text
features/maps/
```

Map business logic.

Examples:

```text
draw polygon
save project
load layers
```

Very important module.

---

## models/

```text
features/models/
```

Model marketplace logic.

Examples:

```text
search models
run model
model details
```

---

## publishers/

```text
features/publishers/
```

Publisher dashboard logic.

Examples:

```text
publish model
edit model
view analytics
```

---

# services/

```text
src/services/
```

Communication layer.

Frontend talks to backend through this folder.

---

## api.ts

```text
services/api.ts
```

Axios instance.

Example:

```ts
api.get("/users")
```

Every API call starts here.

---

## query-client.ts

```text
services/query-client.ts
```

React Query configuration.

Handles:

```text
Caching
Refetching
Invalidation
```

Makes API calls efficient.

---

# store/

```text
src/store/
```

Global frontend state.

Usually Zustand.

Examples:

```text
Current User
Selected Layer
Selected AOI
Theme
```

Accessible anywhere.

---

# hooks/

```text
src/hooks/
```

Custom React hooks.

Examples:

```ts
useAuth()
useMap()
useCurrentUser()
```

Reusable logic.

---

# lib/

```text
src/lib/
```

Utilities and configurations.

Examples:

```text
date formatter
validators
helper functions
map configs
```

Anything not fitting elsewhere.

---

# types/

```text
src/types/
```

TypeScript types.

Examples:

```ts
User
Dataset
MapProject
Publisher
```

Shared across application.

---

# constants/

```text
src/constants/
```

Fixed values.

Examples:

```ts
API_ROUTES
USER_ROLES
MAP_LAYER_TYPES
```

Avoid hardcoding strings everywhere.

---

# Real Example

User clicks:

```text
Run Flood Detection
```

Flow:

```text
app/map/page.tsx
        ↓
features/models/
        ↓
services/api.ts
        ↓
FastAPI
        ↓
Result
        ↓
components/map/
```

---

# One Rule For Frontend

When someone asks:

> Where should I put this code?

Use this:

| Type             | Location    |
| ---------------- | ----------- |
| Page             | app/        |
| Reusable UI      | components/ |
| Business Logic   | features/   |
| API Calls        | services/   |
| Global State     | store/      |
| Custom Hooks     | hooks/      |
| Helper Functions | lib/        |
| TypeScript Types | types/      |
| Constants        | constants/  |

If your team follows this consistently, your frontend won't turn into the typical `"everything inside page.tsx"` disaster.
