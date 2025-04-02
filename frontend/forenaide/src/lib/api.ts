const apiEndpoint = import.meta.env.API_ENDPOINT ?? "http://127.0.0.1:8000";
const supabaseEdgeFunctionEndpoint =
  import.meta.env.SUPABASE_EDGE_FUNCTIONS_ENDPOINT ??
  "http://127.0.0.1:54321/functions/v1";
export { apiEndpoint, supabaseEdgeFunctionEndpoint };
