For your project, use the latest **Next.js + TypeScript + Tailwind + Shadcn UI** from day one.

### 5. Create Folder Structure

```text
src/

├── app/
│   ├── (auth)/
│   ├── dashboard/
│   ├── map/
│   ├── models/
│   └── publishers/
│
├── components/
│   ├── ui/
│   ├── map/
│   ├── layout/
│   └── shared/
│
├── features/
│   ├── auth/
│   ├── users/
│   ├── maps/
│   ├── models/
│   └── publishers/
│
├── services/
│   ├── api.ts
│   └── query-client.ts
│
├── store/
│
├── hooks/
│
├── lib/
│
├── types/
│
└── constants/
```

---

### 6. Setup API Client

`src/services/api.ts`

```ts
import axios from "axios";

export const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL,
});
```

`.env.local`

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

### 7. Setup React Query

```bash
npm install @tanstack/react-query-devtools
```

Create:

```text
src/providers/
├── query-provider.tsx
```

This will handle all API caching and fetching.

---

### 8. First Screens You Need

```text
/
├── Landing
├── Login
├── Register
├── Dashboard
├── Map Viewer
├── Model Marketplace
├── Publisher Dashboard
└── Profile
```

Do not start with fancy authentication, payments, or AI models.

Get this flow working first:

```text
Login
  ↓
Open Map
  ↓
Select Area
  ↓
Submit Job
  ↓
See Result
```

If that pipeline works, the rest of the platform can be built incrementally on top of it.
