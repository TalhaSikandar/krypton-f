<template>
  <section class="section_all bg-light" id="about">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="section_title_all text-center">
            <h3 class="font-weight-bold">
              Empower Your Business - Management at Your Fingertips
            </h3>
            <p class="section_subtitle mx-auto text-muted">
              Take control of your entire operation, from products and raw materials to [mention other management aspects].
            </p>
          </div>
        </div>
      </div>

      <div class="row vertical_content_manage mt-5">
        <div class="col-lg-6">
          <div class="about_header_main mt-3">
            <div class="about_icon_box">
              <p class="text_custom font-weight-bold">
                Simplify Complexity, Manage with Confidence
              </p>
            </div>
            <h4 class="about_heading text-capitalize font-weight-bold mt-4">
              Our platform puts all your business essentials in your hands.
            </h4>
            <p class="text-muted mt-3">
              [Expand on how your platform provides comprehensive management features.]
            </p>
          </div>
        </div>
        <div class="col-lg-6">
          <div class="img_about mt-3">
            <img src="../assets/hero-img.jpg" alt="Management at Your Fingertips" class="img-fluid mx-auto d-block">
          </div>
        </div>
      </div>
    <div class="icons">
      <div class="row mt-3">
        <div class="col-lg-4">
          <div class="about_content_box_all mt-3">
            <div class="about_detail text-center">
              <div class="about_icon">
                <i class="fas fa-box"></i> </div>
              <h5 class="text-dark text-capitalize mt-3 font-weight-bold">
                Product Management
              </h5>
              <p class="edu_desc mt-3 mb-0 text-muted">
                Track inventory, analyze sales trends, and optimize your product offerings.
              </p>
            </div>
          </div>
        </div>

        <div class="col-lg-4">
          <div class="about_content_box_all mt-3">
            <div class="about_detail text-center">
              <div class="about_icon">
                <i class="fas fa-cubes"></i> </div>
              <h5 class="text-dark text-capitalize mt-3 font-weight-bold">
                Raw Material Management
              </h5>
              <p class="edu_desc mb-0 mt-3 text-muted">
                Monitor stock levels, streamline procurement processes, and ensure cost-effectiveness.
              </p>
            </div>
          </div>
        </div>

        <div class="col-lg-4">
          <div class="about_content_box_all mt-3">
            <div class="about_detail text-center">
              <div class="about_icon">
                <i class="fas fa-chart-line"></i> </div>
              <h5 class="text-dark text-capitalize mt-3 font-weight-bold">
                Data-Driven Insights
              </h5>
              <p class="edu_desc mb-0 mt-3 text-muted">
                Gain real-time visibility and make informed decisions based on valuable data.
              </p>
            </div>
          </div>
     </div>   </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'AboutView',
};

</script>
<style scoped>
  /* Paste your CSS styles from the provided HTML here */

  .section_all {
    padding-top: 80px;
    width: 100%;
    padding-bottom: 80px;
    min-height: 100vh;
    display: flex;
  }

  .section-title {
    font-weight: 700; /* Corrected typo from 70 */
  }

  /* Add any other styles from your provided HTML here. 
  Here are some examples of common styles you might find:  */

  .container {
    display: flex;
    width: 1170px;
    margin: 0 auto;
  }

  .row {
    display: flex;
    flex-wrap: wrap;
    margin-right: -15px;
    margin-left: -15px;
  }

  .col-lg-12 {
    flex: 0 0 100%;
    max-width: 100%;
    padding-right: 15px;
    padding-left: 15px;
  }

  .text-center {
    text-align: center;
  }

  .font-weight-bold {
    font-weight: bold;
  }

  .text-muted {
    color: #868e96;
  }

  .mt-3 {
    margin-top: 1rem;
  }

  .img-fluid {
    max-width: 100%;
    height: auto;
  }

  .text_custom {
    color: #e91e63;  /* Example custom color */
  }

  /* Add more styles based on your specific HTML classes and IDs */
</style>
