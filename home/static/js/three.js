import * as THREE from 'https://cdn.skypack.dev/three@0.129.0/build/three.module.js';
import { GLTFLoader } from 'https://cdn.skypack.dev/three@0.129.0/examples/jsm/loaders/GLTFLoader.js';

const camera = new THREE.PerspectiveCamera(
  75, window.innerWidth / (window.innerHeight/2), 0.1, 1000
);

camera.position.z = 3.5;

const scene = new THREE.Scene();
var spaceman;
let mixer;
const loader = new GLTFLoader();
loader.load('https://jjhemmings-portfolio-bucket.s3.eu-north-1.amazonaws.com/static/models/spaceman.glb',
  function (gltf) {
    spaceman = gltf.scene;
    spaceman.position.x = 0;
    spaceman.rotation.y = -3;
    spaceman.rotation.x = 1.1;
    spaceman.rotation.z = -0.1;
    scene.add(spaceman);

    mixer = new THREE.AnimationMixer(spaceman);
    mixer.clipAction(gltf.animations[0]).play();
  },
  function (xhr) {},
  function (error) {
    console.error(error);
  });

const renderer = new THREE.WebGLRenderer({ alpha: true });
renderer.setSize(window.innerWidth, (window.innerHeight/2));
document.getElementById('spaceman').appendChild(renderer.domElement);

const ambientLight = new THREE.AmbientLight(0xffffff, 1.3);
scene.add(ambientLight);

const topLight = new THREE.DirectionalLight(0xffffff, 1);
topLight.position.set(500,500, 500);
scene.add(topLight);

const rerender3D = () => {
  requestAnimationFrame(rerender3D);
  renderer.render(scene, camera);
  if(spaceman) {
    spaceman.rotation.x += 0.002;
    spaceman.rotation.y += 0.001;
    
  // When the user scrolls down increment the spaceman y position
    spaceman.position.z = (window.scrollY / 500);
  }
  if(mixer) mixer.update(0.002);
};

rerender3D();

window.addEventListener('resize', () => {
  renderer.setSize(window.innerWidth, (window.innerHeight/2));
  camera.aspect = window.innerWidth / (window.innerHeight/2);
  camera.updateProjectionMatrix();
})