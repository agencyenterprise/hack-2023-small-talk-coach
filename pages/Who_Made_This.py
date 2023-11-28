import streamlit as st

st.set_page_config(
    page_title="Small talk buddy - Who made this?",
    page_icon="🗣️",
)

who_made_this = """<style>
  :root {
    --text-color: #333333;
  }

  a {
    text-decoration-line: none;
  }

  a:hover {
    text-decoration-line: none;
  }

  .footer {
    width: 56vw;
  position: fixed;
  padding: 1.25rem;
  text-align: center;
  font-size: 0.875rem;
  line-height: 1.25rem;
  bottom: 0;
  background-color: rgb(14, 17, 23);
  }

  .whomadethis-container {
    /* w-full */
    width: 100%;
    /* py-10 */
    padding-top: 2.5rem;
    padding-bottom: 2.5rem;
    /* px-4 */
    padding-left: 2rem;
    padding-right: 2rem;
    /* flex */
    display: flex;
    /* flex-row */
    flex-direction: row;
    /* max-w-full */
    max-width: 80rem;
    margin: auto;
    gap: 2rem;
  }

  .ae-power {
    display: none;
  }

  .text {
    /* mt-8 */
    margin-top: 2rem;

    /* text-2xl */
    font-size: 1.5rem;
    line-height: 2rem;
  }

  .pay-us-btn {
    /* block */
    display: block;
    /* mt-16 py-4 mx-6*/
    padding-top: 1.5rem;
    padding-bottom: 1.5rem;
    margin-left: 1.5rem;
    margin-right: 1.5rem;
    /* font-semibold text-center text-4xl text-gray */
    font-weight: 600;
    text-align: center;
    font-size: 2.25rem;
    color: #333333 !important;
    /* rounded-lg shadow-sm cursor-pointer transition ease-in-out delay-50 duration-300 bg-gradient-to-r from-light-blue to-light-green */
    border-radius: 0.5rem;
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    transition: all 0.3s ease-in-out;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    transition-delay: 50ms;
    transition-duration: 300ms;
    background-image: linear-gradient(to right, #a3dbff, #98e6c2);
  }

  .pay-us-btn:hover {
    transform: translateY(-0.25rem);
    transform: scale(1.1);
    opacity: 0.95;
  }

  .text-orange {
    color: #ff5656;
  }

  .text-gradient {
    /* font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-orange via-pink to-purple */
    font-weight: 800;
    color: transparent;
    -webkit-background-clip: text;
    background-clip: text;
    background-image: linear-gradient(to right, #ff9652, #ff51a5, #ab3ff8);
  }

  .flex-1 {
    flex: 1;
  }

  .logo {
    /* text-3xl */
    font-size: 1.875rem;
    line-height: 2.25rem;
  }

  .whomadethis-article {
    /* max-w-2xl mx-auto */
    max-width: 42rem;
    margin-left: auto;
    margin-right: auto;
  }

  /* sm: */
  @media (min-width: 640px) {
    .logo {
      /* text-4xl */
      font-size: 2.25rem;
      line-height: 2.5rem;
    }

    .container {
      /* px-6 */
      padding-left: 1.5rem;
      padding-right: 1.5rem;
    }
  }

  /* md: */
  @media (min-width: 768px) {
  }

  /* lg: */
  @media (min-width: 1024px) {
    .container {
      /* px-8 */
      padding-left: 2rem;
      padding-right: 2rem;
    }
  }

  /* xl: */
  @media (min-width: 1280px) {
    .ae-power {
      display: flex;
      flex: 1;
      justify-content: center;
    }
  }
</style>
<div>
  <main class="whomadethis-container">
    <div class="flex-1">
      <div class="whomadethis-article">
        <a href="https://ae.studio/same-day-skunkworks" onclick="click()" class="cursor-pointer">
          <img
            alt="AE Logo"
            width="320"
            height="80"
            src="https://ae.studio/img/aestudio-logo-dark.svg"
          />
        </a>
        <p class="text">
          Through our <span class="text-orange">Skunkworks Division</span>, we
          build pretty cool products, like the one you just checked out.
        </p>
        <p class="text">
          We also build cutting-edge software and AI to
          <span class="text-gradient">
            solve the most challenging problems
          </span>
          facing our clients through our product studio.
        </p>
      </div>
    </div>
    <div class="ae-power">
      <img
        alt="AE Power"
        width="300"
        src="https://www.samedayskunkworks.com/ae-power.svg"
      />
    </div>
  </main>
    <a
        href="https://form.typeform.com/to/PJAvghq3"
        target="_black"
        rel="noreferrer"
        class="pay-us-btn"
    >
        Pay us to build things
    </a>
  <div class="footer">
    <a
      style="color: white"
      href="https://ae.studio?utm_source=smalltalkbuddy.com"
      target="_blank"
    >
      Made with ❤️ by <span style="text-decoration-line: underline;">AE Studio</span>
    </a>
  </div>
</div>
<script>
  function click() {
    alert("you clicked the logo");
    fetch('https://www.samedayskunkworks.com/api/analytics/addEvent', {
      method: 'post',
      body: JSON.stringify({
        origin: window.location.href,
        destination: 'https://ae.studio/same-day-skunkworks',
        event: 'SDS Utils Click - Who made this section',
      }),
    });
  }
</script>
"""
st.markdown(who_made_this, unsafe_allow_html=True)
