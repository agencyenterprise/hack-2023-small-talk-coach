import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Small talk buddy - Pricing",
    page_icon="🗣️",
)

st.image("ideogram.jpeg")
pricing = """<style>
  :root {
    --primary: #047857;
    --icon-color: #047857;
    --border-color: #047857;
    --text-color: black;
    --free-bg-color: #eee;
    --ae-bg-color: #eee;
    --btn-outlined-color: #047857;
    --btn-bg-color: #047857;
    --btn-color: white;
    --badge-color: white;
    --badge-bg-color: #047857;
  }

  a {
    text-decoration-line: none;
  }

  a:hover {
    text-decoration-line: none;
  }

  footer {
    text-align: center;
    font-size: 0.875rem;
    line-height: 1.25rem;
    margin-top: 2rem;
  }

  ul {
    display: flex;
    flex-direction: column;
    margin-top: 2rem;
    margin-bottom: 0;
    font-size: 0.875rem;
    line-height: 1.5rem;
    list-style: none;
    padding-left: 0;
    gap: 0.5rem;
  }

  li {
    display: flex;
    gap: 0.5rem;
    align-items: center;
  }

  .pricing-container {
    /* w-full */
    width: 100%;
    /* py-10 */
    padding-top: 2.5rem;
    padding-bottom: 2.5rem;
    /* px-4 */
    padding-left: 1rem;
    padding-right: 1rem;
    /* flex */
    display: flex;
    /* flex-row */
    flex-direction: row;
    /* max-w-full */
    max-width: 100%;
  }

  .pricing-section {
    margin-left: auto;
    margin-right: auto;
    max-width: 80rem;
  }

  .tiers-container {
    /* flex flex-col justify-center mx-auto mt-16 isolate gap-y-8  */
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-left: auto;
    margin-right: auto;
    gap: 2rem;
    isolation: isolate;
  }

  .tier {
    /* flex flex-col justify-between rounded-3xl p-8 xl:p-10 */
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    border-radius: 1rem;
    padding: 1.5rem;
    color: var(--text-color);
    flex: 1;
  }

  .tier .price {
    /* flex items-baseline mt-6 gap-x-1 */
    display: flex;
    align-items: baseline;
    margin-top: 1.5rem;
    gap: 0.25rem;
  }

  .tier .subtitle {
    margin-top: 1rem;
    font-size: 0.875rem;
    line-height: 1.5rem;
    text-align: center;
  }

  .tier .header {
    /* flex items-center justify-between gap-x-4 */
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
  }

  .tier .header .title {
    /* text-lg font-semibold leading-8 */
    font-size: 1.125rem;
    font-weight: 600;
    line-height: 1.75rem;
    margin: 0;
    /* color */
    color: var(--primary);
  }

  .price .price-value {
    /* text-4xl font-bold tracking-tight */
    font-size: 2.25rem;
    font-weight: 700;
    letter-spacing: -0.025em;
  }

  .price .price-period {
    /* text-sm leading-6 */
    font-size: 0.875rem;
    line-height: 1.5rem;
  }

  .icon {
    /* flex-none w-5 h-5 */
    flex: none;
    width: 1.25rem;
    height: 1.25rem;
    color: var(--icon-color);
  }

  .free-tier {
    /* color: var(--text-color); */
    background-color: var(--free-bg-color);
    border: 2px solid var(--border-color);
  }

  .free-tier-title {
    color: var(--text-color) !important;
  }

  .ae-tier {
    /* lg:rounded-b-none lg:rounded-l-none xl:p-10 */
    background-color: var(--ae-bg-color);
    border: 2px solid var(--border-color);
  }

  .tier .header .badge {
    /* rounded-full py-1 px-2.5 text-xs font-semibold leading-5 */
    border-radius: 9999px;
    padding-top: 0.25rem;
    padding-bottom: 0.25rem;
    padding-left: 0.625rem;
    padding-right: 0.625rem;
    font-size: 0.75rem;
    font-weight: 600;
    line-height: 1.25rem;
    margin: 0;
    /* color */
    background: var(--badge-bg-color);
    opacity: 0.5;
    color: var(--badge-color);
  }

  .btn-outlined {
    /* shadow-sm mt-8 block rounded-md py-2 px-3 text-center text-sm font-semibold leading-6 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 cursor-pointer */
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    margin-top: 2rem;
    display: block;
    border-radius: 0.375rem;
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
    padding-left: 0.75rem;
    padding-right: 0.75rem;
    font-size: 0.875rem;
    font-weight: 600;
    line-height: 1.5rem;
    text-align: center;
    cursor: pointer;
    /* color */
    background-color: transparent;
    border: 2px solid var(--btn-outlined-color);
    color: var(--btn-outlined-color) !important;
  }

  .btn {
    /* shadow-sm mt-8 block rounded-md py-2 px-3 text-center text-sm font-semibold leading-6 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 cursor-pointer */
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    margin-top: 2rem;
    display: block;
    border-radius: 0.375rem;
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
    padding-left: 0.75rem;
    padding-right: 0.75rem;
    font-size: 0.875rem;
    font-weight: 600;
    line-height: 1.5rem;
    text-align: center;
    cursor: pointer;
    /* color */
    background-color: var(--btn-bg-color);
    border: 2px solid var(--btn-bg-color);
    color: var(--btn-color) !important;
  }

  .btn:hover {
    opacity: 75%;
  }

  .w-full {
    width: 100%;
  }

  /* sm: */
  @media (min-width: 640px) {
  }

  /* md: */
  @media (min-width: 768px) {
    .tiers-container {
      flex-direction: row;
      gap: 0;
    }
  }

  /* lg: */
  @media (min-width: 1024px) {
    .tiers-container {
      margin-left: 0;
      margin-right: 0;
      max-width: none;
    }

    .ae-tier {
      /* rounded-b-none rounded-l-none xl:p-10 */
      border-bottom-left-radius: 0;
      border-top-left-radius: 0;
      border-bottom-right-radius: 0;
    }

    /* lg:mt-8 lg:rounded-r-none xl:p-10 */
    .free-tier {
      margin-top: 2rem;
      border-top-right-radius: 0;
      border-bottom-right-radius: 0;
      border-right: none;
    }
  }

  /* xl: */
  @media (min-width: 1280px) {
    .free-tier {
      padding: 2.5rem;
    }
    .ae-tier {
      padding: 2.5rem;
    }
  }


</style>
<main>
  <h2
    style="
      padding: 4rem 2rem 2rem;
      max-width: 80rem;
      margin: auto;
      color: white;
      text-align: center;
    "
  >
    Simple pricing, no commitment
  </h2>
  <main class="pricing-container">
    <div class="pricing-section">
      <div class="tiers-container">
        <!-- FREE TIER -->
        <div class="tier free-tier">
          <div>
            <div class="header">
              <h3 class="title free-tier-title">Free</h3>
            </div>
            <p class="subtitle">Completely free, forever.</p>
            <p class="price">
              <span class="price-value">$0</span>
              <span class="price-period">/month</span>
            </p>
            <ul role="list">
              <li>
                <svg fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" class="icon">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
                Refreshable prompts
              </li>
              <li>
                <svg fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" class="icon">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
                Interactive practice platform
              </li>
              <li>
                <svg fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" class="icon">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
                Real-Time feedback
              </li>
              <li>
                <svg fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" class="icon">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
                Accessible anytime
              </li>
            </ul>
          </div>
          <a
            href="https://form.typeform.com/to/PJAvghq3"
            target="_blank"
            rel="noreferrer"
            class="btn-outlined"
          >
            Current plan
          </a>
        </div>
        <!-- AE TIER -->
        <div class="tier ae-tier">
          <div>
            <div class="header">
              <h3 class="title">Enterprise</h3>
              <p class="badge">Most popular</p>
            </div>
            <p class="subtitle">
              AE Studio can build cool things like this for you too.
            </p>
            <p class="price">
              <span class="price-value">$x</span>
              <span class="price-period">/month</span>
            </p>
            <ul role="list">
              <li>
                <svg fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" class="icon">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
                Software Development
              </li>
              <li>
                <svg fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" class="icon">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
                Data Science
              </li>
              <li>
                <svg fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" class="icon">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
                Product Design
              </li>
              <li>
                <svg fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" class="icon">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
                Brain-Computer Interfaces
              </li>
              <li>
                <svg fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" class="icon">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
                AI
              </li>
              <li>
                <svg fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" class="icon">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
                Let's talk!
              </li>
            </ul>
          </div>
          <a href="https://form.typeform.com/to/PJAvghq3" target="_blank" rel="noreferrer" class="btn">
            Pay us to build things
          </a>
        </div>
      </div>
    </div>
  </main>
  <footer>
    <a
      style="color: white"
      href="https://ae.studio?utm_source=smalltalkbuddy.com"
      target="_blank"
    >
      Made with ❤️ by <span style="text-decoration-line: underline;">AE Studio</span>
    </a>
  </footer>
</main>
"""
st.markdown(pricing, unsafe_allow_html=True)

html(
    """<script src="https://scripts.simpleanalyticscdn.com/latest.js"></script>"""
)
