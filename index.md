## Welcome to My Page

You can use the [bakoriharsh@gmail.com](https://mail.google.com/mail/?view=cm&fs=1&to=bakoriharsh@gmail.com.com&su=Contacted using Github linck&body=Dear Mr.Harsh, ) to contact me. 

<a href="#">
  <img align="center" src="https://github-readme-stats.vercel.app/api?username=harshbakori&theme=dark&show_icons=true" />
</a>

<style>
* {
  font-family: Consolas, "Andale Mono WT", "Andale Mono", "Lucida Console",
    "Lucida Sans Typewriter", "DejaVu Sans Mono", "Bitstream Vera Sans Mono",
    "Liberation Mono", "Nimbus Mono L", Monaco, "Courier New", Courier,
    monospace;
}

$blue: #29b6f6;
$green: #9ccc65;
$purple: #ba68c8;
$orange: #f57c00;
$red: #ef5350;
$cyan: #4dd0e1;
$background-light: #ffa726;
$background-dark: #ff9800;

body {
  background-image: linear-gradient(
    to bottom right,
    $background-dark,
    $background-light
  );
}

@mixin text-color($color) {
  color: $color;
}

.blue {
  @include text-color($blue);
}

.green {
  @include text-color($green);
}

.purple {
  @include text-color($purple);
}

.cyan {
  @include text-color($cyan);
}

.red {
  @include text-color($red);
}

.content {
  height: 100vh;
  @include text-color(white);

  display: flex;
  justify-content: center;
  align-items: center;
}

.card {
  //FUNCTIONALITY
  perspective: 150rem;
  height: 20rem;
  width: 30rem;

  position: relative;

  &__side {
    height: 15rem;
    transition: all 0.8s ease;

    position: absolute;
    top: 0;
    left: 0;
    margin: auto;
    width: 30rem;

    backface-visibility: hidden;
    border-radius: 3px;
    overflow: hidden;
    box-shadow: 0 1.5rem 4rem rgba(black, 0.4);

    &--front {
      background-color: #1c1c1c;
    }

    &--back {
      transform: rotateY(180deg);

      background-color: #1c1c1c;
    }
  }

  &:hover &__side--front {
    transform: rotateY(-180deg);
  }

  &:hover &__side--back {
    transform: rotateY(0deg);
  }

  //FRONT SIDE STYLING
  &__cont {
    height: 15rem;
    background-color: #1c1c1c;

    display: flex;
    align-items: center;
    justify-content: center;
  }

  &__cta {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 90%;
    @include text-color(white);

    p {
      margin-left: 1rem;

      & > .space {
        margin-left: 2rem;
      }
    }
  }
}

</style>

<div class="content">
  <div class="card">
    <div class="card__side card__side--front">
      <!-- Front Content -->
      <div class="card__cont">
        <span class="blue">alert</span>
        <span>(<span class="green">'Hello World!'</span>)</span>
      </div>
    </div>
    <div class="card__side card__side--back">
      <!-- Back Content -->
      <div class="card__cta">
        <p><span class="purple">const</span> aboutMe <span class="cyan">=</span> {
          <br />
          <span class="space red">name</span>
          <span class="cyan">:</span> <span class="green">'laura pinto'</span>,
          <br/>
          <span class="space red">email</span>
          <span class="cyan">:</span> <span class="green">'lauraalpinto@gmail.com</span>',
          <br/>
          <span class="space red">position</span>
          <span class="cyan">:</span>
          <span class="green">'front-end developer'</span>,
          <br/>
          <span class="space red">website</span><span class="cyan">:</span> <span class="green">'lauraalpinto.github.io'</span>
          <br/> 
          };
        </p>
      </div>
    </div>
  </div>
